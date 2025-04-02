from sqlite3 import connect

def apply_bcnf_changes():
    conn = connect('library.db')
    cur = conn.cursor()

    # Drop old non-BCNF tables if they exist
    cur.execute('DROP TABLE IF EXISTS PrintBooks;')
    cur.execute('DROP TABLE IF EXISTS BookMetadata;')
    cur.execute('DROP TABLE IF EXISTS Registered;')

    # Create BCNF-compliant BookMetadata table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS BookMetadata (
        ISBN TEXT PRIMARY KEY,
        publisher TEXT,
        author TEXT
    );
    ''')

    # Create BCNF-compliant PrintBooks table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS PrintBooks (
        item_id INTEGER PRIMARY KEY,
        ISBN TEXT,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (ISBN) REFERENCES BookMetadata(ISBN)
    );
    ''')

    # Create BCNF-compliant Registered table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Registered (
        event_id INTEGER,
        volunteer_id INTEGER,
        PRIMARY KEY (event_id, volunteer_id),
        FOREIGN KEY (event_id) REFERENCES LibraryEvents(event_id),
        FOREIGN KEY (volunteer_id) REFERENCES Volunteer(volunteer_id)
    );
    ''')

    conn.commit()
    conn.close()

apply_bcnf_changes()
