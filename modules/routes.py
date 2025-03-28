# ----------------------------
# Query logic & Requests
# ----------------------------
from flask import Flask, render_template, url_for, request
import sqlite3

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html', template_folder='../templates')

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

