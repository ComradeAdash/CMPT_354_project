# ----------------------------
# Query logic & Requests
# ----------------------------
from flask import Flask, render_template, url_for, request
import sqlite3

def init_routes(app):

    
    # Utility Methods

    def get_row_count(tableName):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute(f'''
            SELECT COUNT(*)
            FROM {tableName}
        ''')
        user_amnt = cur.fetchone()[0]
        conn.close()
        return user_amnt
    
    # ----------------------------

    @app.route('/')
    def index():
        return render_template('index.html', template_folder='../templates')

    @app.route('/findEvent')
    def show_events():
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT *
            FROM LibraryEvents le
        ''')
        events = cur.fetchall()
        conn.close()
        return render_template('findEvent.html', events=events)

    @app.route('/items')
    def show_items():
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()

        # Pull basic item info + left join subtype tables
        cur.execute('''
            SELECT li.item_id, li.title, li.available_copies,
                pb.ISBN, pb.publisher, pb.author,
                r.format, r.artist
            FROM LibraryItems li
            LEFT JOIN PrintBooks pb ON li.item_id = pb.item_id
            LEFT JOIN Records r ON li.item_id = r.item_id
        ''')
        items = cur.fetchall()
        conn.close()
        return render_template('items.html', items=items)
    
    @app.route('/find', methods=['GET', 'POST'])
    def find_item():
        results = []
        if request.method == 'POST':
            search_query = request.form['title']
            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute('''
                SELECT li.item_id, li.title, li.available_copies,
                    pb.ISBN, pb.publisher, pb.author
                FROM LibraryItems li
                LEFT JOIN PrintBooks pb ON li.item_id = pb.item_id
                WHERE li.title LIKE ?
            ''', (f'%{search_query}%',))
            results = cur.fetchall()
            conn.close()
        return render_template('find.html', results=results)
        
    @app.route('/findEvent', methods=['GET', 'POST'])
    def find_event():
        eventResults = []
        if request.method == 'POST':
            search_query = request.form['title']
            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute('''
                SELECT *
                FROM LibraryEvents le
                WHERE le.title LIKE ?
            ''', (f'%{search_query}%',))
            eventResults = cur.fetchall()
            conn.close()
        return render_template('findEvent.html', eventResults=eventResults)

    @app.route('/registerEvent', methods=['GET', 'POST'])
    def register_event():
        # we get the user to fill in their information on the html form
        # this information will be inserted and then they can select an event to register for (we will fill in the registered table)
         if request.method == 'POST':
            search_query = request.form['title']
            conn = sqlite3.connect('library.db')
            user = (get_row_count(LibraryUsers) + 1,request.form['name'],request.form['email'],request.form['phone'])
            cur = conn.cursor()
        
            cur.execute('''
                INSERT INTO LibraryUsers (user_id, name, email, phone_number) VALUES (?, ?, ?, ?)"
            ''',user)
            conn.close()
            return

    # ask_librarian and volunteer will be popups on the the homepage. 
    @app.route('/index', methods=['GET', 'POST'])
    def ():
        pass

    @app.route('/index', methods=['GET', 'POST'])
    def ask_librarian():
        pass

    @app.route('/index', methods=['GET', 'POST'])
    def volunteer():
        pass