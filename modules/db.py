# ----------------------------
# Global DB connection & Relations
# ----------------------------
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('library.db')  
    cur = conn.cursor()

    # create and fill in the relations with data. 
    pass