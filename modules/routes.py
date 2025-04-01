# ----------------------------
# Query logic & Requests
# ----------------------------
from flask import Flask, render_template, url_for, request, redirect
import sqlite3

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html', template_folder='../templates')
    
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
                r.format, r.artist,
                m.ISSN,
                ob.ISBN,
                cd.genre
            FROM LibraryItems li
            LEFT JOIN PrintBooks pb ON li.item_id = pb.item_id
            LEFT JOIN BookMetadata bm ON pb.ISBN = bm.ISBN
            LEFT JOIN Records r ON li.item_id = r.item_id
            LEFT JOIN Magazines m ON li.item_id = m.item_id
            LEFT JOIN OnlineBooks ob ON li.item_id = ob.item_id
            LEFT JOIN CDs cd ON li.item_id = cd.item_id
        '''

        params = ()
        if search_query:
            query += ' WHERE li.title LIKE ?'
            params = (f'%{search_query}%',)

        cur.execute(query, params)
        results = cur.fetchall()
        conn.close()

        return render_template('find.html', results=results, search_query=search_query, message=request.args.get('message'))


    
    @app.route('/borrow', methods=['POST'])
    def borrow_item():
        item_id = request.form['item_id']
        user_id = request.form['user_id']

        conn = sqlite3.connect('library.db')
        cur = conn.cursor()

        # Insert into Borrow table
        cur.execute('''
            INSERT INTO Borrow (item_id, user_id, borrow_status, due_date, fine_amnt)
            VALUES (?, ?, 'borrowed', date('now', '+14 days'), 0)
        ''', (item_id, user_id))

        # Decrease available copies - 1
        cur.execute('''
            UPDATE LibraryItems SET available_copies = available_copies - 1
            WHERE item_id = ? AND available_copies > 0
        ''', (item_id,))

        conn.commit()
        conn.close()

        return redirect(url_for('find_item', message='Item borrowed successfully!'))
    
    @app.route('/return', methods=['GET', 'POST'])
    def return_item():
        message = ''
        borrowed_items = []
        user_id = ''

        if request.method == 'POST':
            user_id = request.form['user_id']
            item_id = request.form.get('item_id')  # only filled if returning

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()

            # If the user clicked "Return"
            if item_id:
                cur.execute('SELECT * FROM Borrow WHERE user_id = ? AND item_id = ?', (user_id, item_id))
                borrowed = cur.fetchone()

                if borrowed:
                    cur.execute('DELETE FROM Borrow WHERE user_id = ? AND item_id = ?', (user_id, item_id))
                    cur.execute('UPDATE LibraryItems SET available_copies = available_copies + 1 WHERE item_id = ?', (item_id,))
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

            conn.commit()
            conn.close()

        return render_template('return.html', message=message, borrowed_items=borrowed_items, user_id=user_id)


    @app.route('/donate', methods=['GET', 'POST'])
    def donate_item():
        message = ''
        if request.method == 'POST':
            title = request.form['title']
            copies = int(request.form['copies'])
            item_type = request.form['type']

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()

            # Insert into LibraryItems
            cur.execute('INSERT INTO LibraryItems (title, available_copies) VALUES (?, ?)', (title, copies))
            item_id = cur.lastrowid

            # Insert into appropriate subtype
            if item_type == 'PrintBooks':
                isbn = request.form.get('isbn')
                publisher = request.form.get('publisher')
                author = request.form.get('author')

                # 1. Insert into BookMetadata (ignore if ISBN already exists)
                cur.execute('''
                    INSERT OR IGNORE INTO BookMetadata (ISBN, publisher, author)
                    VALUES (?, ?, ?)
                ''', (isbn, publisher, author))

                # 2. Link item to ISBN
                cur.execute('INSERT INTO PrintBooks (item_id, ISBN) VALUES (?, ?)', (item_id, isbn))

            elif item_type == 'Records':
                format = request.form.get('format')
                artist = request.form.get('artist')
                cur.execute('INSERT INTO Records (item_id, format, artist) VALUES (?, ?, ?)', 
                            (item_id, format, artist))

            elif item_type == 'Magazines':
                issn = request.form.get('issn')
                cur.execute('INSERT INTO Magazines (item_id, ISSN) VALUES (?, ?)', (item_id, issn))

            elif item_type == 'OnlineBooks':
                isbn = request.form.get('online_isbn')
                cur.execute('INSERT INTO OnlineBooks (item_id, ISBN) VALUES (?, ?)', (item_id, isbn))

            elif item_type == 'CDs':
                genre = request.form.get('genre')
                cur.execute('INSERT INTO CDs (item_id, genre) VALUES (?, ?)', (item_id, genre))

            conn.commit()
            conn.close()

            message = f'Thank you for donating "{title}"!'

        return render_template('donate.html', message=message)
