# ----------------------------
# Query logic & Requests
# ----------------------------
from flask import Flask, render_template, url_for, request, redirect, make_response
import sqlite3

def init_routes(app):

    # handles user logins, redirects to the homepage after a succesful login
    @app.route('/', methods=['GET', 'POST'])
    def login():
        print("Hello")

        results = []
        if request.method == 'POST':
            name = request.form['name']
            user_id = request.form['user_id']
            print(name)

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()

            cur.execute('''
                SELECT * FROM LibraryUsers lu WHERE (lu.user_id = ?) AND (lu.name = ?)
            ''',(user_id,name))
            results = cur.fetchall()

            if results:
                # The user exists, we can safely login
                print("user found")
                resp = make_response(redirect(url_for('index')))
                conn.commit()
                conn.close()
                return resp  

        return render_template('login.html', template_folder='../templates')

    # homepage, contains navigation for all library services
    @app.route('/home')
    def index():
        return render_template('index.html', template_folder='../templates')
   
    # users who don't have an account can create one, before getting access to the library features. 
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        message = ""
        if request.method == 'POST':
            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            try: 
                email = request.form['email']
                name = request.form['name']
                phone_num = request.form['phone']

                cur.execute('''
                    INSERT INTO LibraryUsers (name,email,phone_number) VALUES (?, ?, ?);
                ''',(name,email,phone_num))
                user_id = cur.lastrowid
                conn.commit()
                conn.close()
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")
                return render_template('register.html', message="User Already Exists")

            return render_template('register.html', success=True, template_folder='../templates', message=f"{user_id}")

        return render_template('register.html', success=False, template_folder='../templates',message=message)

    # filtering and searching through library items
    @app.route('/find', methods=['GET', 'POST'])
    def find_item():
        search_query = ''
        if request.method == 'POST':
            search_query = request.form['title']

        conn = sqlite3.connect('library.db')
        cur = conn.cursor()

        query = '''
            SELECT li.item_id, li.title, li.available_copies,
                pb.ISBN, bm.publisher, bm.author,
                COALESCE(mm1.format, mm2.format) AS format,
                COALESCE(mm1.artist, mm2.artist) AS artist,
                m.ISSN,
                ob.ISBN AS ob_ISBN, ob.url,
                COALESCE(mm2.genre, mm1.genre) AS genre
            FROM LibraryItems li
            LEFT JOIN PrintBooks pb ON li.item_id = pb.item_id
            LEFT JOIN BookMetadata bm ON pb.ISBN = bm.ISBN
            LEFT JOIN Records r ON li.item_id = r.item_id
            LEFT JOIN MediaMetadata mm1 ON r.media_id = mm1.media_id
            LEFT JOIN Magazines m ON li.item_id = m.item_id
            LEFT JOIN OnlineBooks ob ON li.item_id = ob.item_id
            LEFT JOIN CDs cd ON li.item_id = cd.item_id
            LEFT JOIN MediaMetadata mm2 ON cd.media_id = mm2.media_id
        '''


        params = ()
        if search_query:
            query += ' WHERE li.title LIKE ?'
            params = (f'%{search_query}%',)

        cur.execute(query, params)
        results = cur.fetchall()
        conn.close()

        return render_template('find.html', results=results, search_query=search_query, message=request.args.get('message'))

    # query logic for borrowing an item
    @app.route('/borrow', methods=['POST'])
    def borrow_item():
        try:
            item_id = request.form['item_id']
            user_id = request.form['user_id']

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()

            cur.execute('''
                INSERT INTO Borrow (item_id, user_id, borrow_status, due_date, fine_amnt)
                VALUES (?, ?, 'borrowed', date('now', '+14 days'), 0)
            ''', (item_id, user_id))

            # cur.execute('''
            #     UPDATE LibraryItems SET available_copies = available_copies - 1
            #     WHERE item_id = ? AND available_copies > 0
            # ''', (item_id,)

        except sqlite3.IntegrityError as e:
            print(f"Integrity Error: {e}")
            return redirect(url_for('find_item', message='There are no Copies Available Sorry!'))

        conn.commit()
        conn.close()
        
        return redirect(url_for('find_item', message='Item borrowed successfully!'))
    
    # query logic for returning an item
    @app.route('/return', methods=['GET', 'POST'])
    def return_item():
        message = ''
        borrowed_items = []
        user_id = ''

        if request.method == 'POST':
            user_id = request.form['user_id']
            item_id = request.form.get('item_id')

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()

            # If the user clicked "Return"
            if item_id:
                cur.execute('SELECT * FROM Borrow WHERE user_id = ? AND item_id = ?', (user_id, item_id))
                borrowed = cur.fetchone()

                if borrowed:
                    # Only delete one row (in case multiple are borrowed)
                    cur.execute('''
                        DELETE FROM Borrow 
                        WHERE rowid IN (
                            SELECT rowid FROM Borrow 
                            WHERE user_id = ? AND item_id = ?
                            LIMIT 1
                        )
                    ''', (user_id, item_id))
                    # cur.execute('UPDATE LibraryItems SET available_copies = available_copies + 1 WHERE item_id = ?', (item_id,))
                    conn.commit()
                    message = 'Item returned successfully!'
                else:
                    message = 'You cannot return an item you didn’t borrow.'

            # Get all current borrowings for this user
            cur.execute('''
                SELECT li.item_id, li.title, li.available_copies, COUNT(*) as copies_borrowed
                FROM Borrow b
                JOIN LibraryItems li ON b.item_id = li.item_id
                WHERE b.user_id = ?
                GROUP BY li.item_id, li.title, li.available_copies
            ''', (user_id,))

            borrowed_items = cur.fetchall()
            conn.close()

        return render_template('return.html', message=message, borrowed_items=borrowed_items, user_id=user_id)

      
    # query logic for making a donation
    @app.route('/donate', methods=['GET', 'POST'])
    def donate_item():
        message = ''
        if request.method == 'POST':
            title = request.form['title']
            copies = int(request.form['copies'])
            item_type = request.form['type']

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()

            cur.execute('INSERT INTO LibraryItems (title, available_copies) VALUES (?, ?)', (title, copies))
            item_id = cur.lastrowid

            if item_type == 'PrintBooks':
                isbn = request.form.get('isbn')
                publisher = request.form.get('publisher')
                author = request.form.get('author')

                cur.execute('''
                    INSERT OR IGNORE INTO BookMetadata (ISBN, publisher, author)
                    VALUES (?, ?, ?)
                ''', (isbn, publisher, author))

                cur.execute('INSERT INTO PrintBooks (item_id, ISBN) VALUES (?, ?)', (item_id, isbn))

            elif item_type == 'Records':
                format = request.form.get('format')
                artist = request.form.get('artist')
                genre = 'Unknown'
                cur.execute('INSERT INTO MediaMetadata (format, artist, genre) VALUES (?, ?, ?)', (format, artist, genre))
                media_id = cur.lastrowid
                cur.execute('INSERT INTO Records (item_id, media_id) VALUES (?, ?)', (item_id, media_id))

            elif item_type == 'Magazines':
                issn = request.form.get('issn')
                cur.execute('INSERT INTO Magazines (item_id, ISSN) VALUES (?, ?)', (item_id, issn))

            elif item_type == 'OnlineBooks':
                isbn = request.form.get('online_isbn')
                url = request.form.get('url', 'http://example.com')  # fallback default
                cur.execute('INSERT INTO OnlineBooks (item_id, url, ISBN) VALUES (?, ?, ?)', (item_id, url, isbn))

            elif item_type == 'CDs':
                genre = request.form.get('genre')
                format = 'CD'
                artist = 'Unknown'
                cur.execute('INSERT INTO MediaMetadata (format, artist, genre) VALUES (?, ?, ?)', (format, artist, genre))
                media_id = cur.lastrowid
                cur.execute('INSERT INTO CDs (item_id, media_id) VALUES (?, ?)', (item_id, media_id))

            conn.commit()
            conn.close()
            message = f'Thank you for donating "{title}"!'

        return render_template('donate.html', message=message)

    # filtering and searching through events
    @app.route('/findEvent', methods=['GET', 'POST'])
    def find_event():
        search_query = ''
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        if request.method == 'POST':
            search_query = request.form['title']

        query = ('''
            SELECT *
            FROM LibraryEvents le
        ''')

        params = ()
        if search_query:
            query += ' WHERE le.title LIKE ?'
            params = (f'%{search_query}%',)

        cur.execute(query, params)
        eventResults = cur.fetchall()
        conn.close()
        return render_template('findEvent.html', eventResults=eventResults,search_query=search_query, message=request.args.get('message'))
        
    # query logic for registering for an event
    @app.route('/registerEvent', methods=['GET', 'POST'])
    def register_event():
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        try:
            if request.method == 'POST':
                user_id = request.form['user_id']
                event_id = request.form['event_id']

                # insert the User into the event. 
                cur.execute('''
                    INSERT INTO Attend (event_id, user_id) 
                    VALUES (?, ?)
                ''', (event_id, user_id))

                conn.commit()
                conn.close()

        except sqlite3.IntegrityError as e:
            print(f"Integrity Error: {e}")
            return redirect(url_for('find_event', message='You have already registered for the event!'))

        return redirect(url_for(f'find_event', message='You Have Succesfully Registered for the event!'))
    
    # query logic for volunteering for an event
    @app.route('/volunteer', methods=['GET', 'POST'])
    def volunteer_event():
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        try: 
            if request.method == 'POST':
                user_id = request.form['user_id']
                event_id = request.form['event_id']
                print(user_id)
                print(event_id)
                cur.execute('''
                    INSERT INTO Volunteer (event_id,user_id) VALUES (?,?);
                ''',(event_id,user_id,))

                conn.commit()
                conn.close()

        except sqlite3.IntegrityError as e:
            print(f"Integrity Error: {e}")
            return redirect(url_for('find_event', message='You have already volunteered for the event!'))

        return redirect(url_for(f'find_event', message='You Have Successfully Volunteered to help for the event!'))

    # query logic for librarian help, getting help requests etc. 
    @app.route('/help', methods=['GET', 'POST'])
    def ask_librarian():
        message = ''
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        if request.method == 'POST':
            user_id = request.form['user_id']
            text_info = request.form['text_info']
            print(user_id)
            print(text_info)
            
            # we query the personnel for users who are librarians, then we insert a random one to help with the ticket. 
            cur.execute('''
                SELECT * FROM Personnel p WHERE (p.role = "Librarian") ORDER BY RANDOM() LIMIT 1
            ''')
            personnel = cur.fetchone()
            personnel_id = personnel[0]
            personnel_name = personnel[1]
            print(f"Lbrarian {personnel_name} with ID:{personnel_id}\n")

            cur.execute('''
                INSERT INTO SupportTickets (personnel_ID,user_id,text_info) VALUES (?, ?, ?);
            ''',(personnel_id, user_id,text_info,))

            conn.commit()
            conn.close()

        return render_template('help.html')
