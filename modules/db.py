# ----------------------------
# Global DB connection & Relations
# ----------------------------
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('library.db')  
    cur = conn.cursor()

    # create and fill in the relations with data. 
    
    # ========== USERS ==========
    # Library Users
    cur.execute('''
    CREATE TABLE IF NOT EXISTS LibraryUsers (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone_number TEXT
    );
    ''')
    
    # Personnel
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Personnel (
        personnel_ID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        role TEXT CHECK(role IN ('Manager', 'Librarian', 'IT'))
    );
    ''')

    # WorksFor
    cur.execute('''
    CREATE TABLE IF NOT EXISTS WorksFor (
        user_id INTEGER,
        personnel_ID INTEGER,
        PRIMARY KEY (user_id, personnel_ID),
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id),
        FOREIGN KEY (personnel_ID) REFERENCES Personnel(personnel_ID)
    );
    ''')

    # Volunteer
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Volunteer (
        volunteer_id INTEGER PRIMARY KEY,
        event_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (event_id) REFERENCES LibraryEvents(event_id),
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id)
    );
    ''')

    # ========== LIBRARY ITEMS & TYPES (Revised BCNF-compliant) ==========

    # Core table for all library items
    cur.execute('''
    CREATE TABLE IF NOT EXISTS LibraryItems (
        item_id INTEGER PRIMARY KEY,
        available_copies INTEGER CHECK(available_copies >= 0),
        title TEXT NOT NULL
    );
    ''')

    # Book metadata (shared by PrintBooks & OnlineBooks)
    cur.execute('''
    CREATE TABLE IF NOT EXISTS BookMetadata (
        ISBN TEXT PRIMARY KEY,
        publisher TEXT,
        author TEXT
    );
    ''')

    # Media metadata (shared by CDs and Records)
    cur.execute('''
    CREATE TABLE IF NOT EXISTS MediaMetadata (
        media_id INTEGER PRIMARY KEY,
        format TEXT,
        artist TEXT,
        genre TEXT
    );
    ''')

    # Subtype: Print Books
    cur.execute('''
    CREATE TABLE IF NOT EXISTS PrintBooks (
        item_id INTEGER PRIMARY KEY,
        ISBN TEXT,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (ISBN) REFERENCES BookMetadata(ISBN)
    );
    ''')

    # Subtype: Online Books
    cur.execute('''
    CREATE TABLE IF NOT EXISTS OnlineBooks (
        item_id INTEGER PRIMARY KEY,
        url TEXT,
        ISBN TEXT,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (ISBN) REFERENCES BookMetadata(ISBN)
    );
    ''')

    # Subtype: Magazines
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Magazines (
        item_id INTEGER PRIMARY KEY,
        ISSN TEXT,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id)
    );
    ''')

    # Subtype: CDs
    cur.execute('''
    CREATE TABLE IF NOT EXISTS CDs (
        item_id INTEGER PRIMARY KEY,
        media_id INTEGER,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (media_id) REFERENCES MediaMetadata(media_id)
    );
    ''')
    
    # Subtype: Records
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Records (
        item_id INTEGER PRIMARY KEY,
        media_id INTEGER,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (media_id) REFERENCES MediaMetadata(media_id)
    );
    ''')

    # ========== BORROWING ==========

    # Borrow
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Borrow (
        borrow_id INTEGER PRIMARY KEY,
        item_id INTEGER,
        user_id INTEGER,
        borrow_status TEXT,
        due_date TEXT,
        fine_amnt REAL,
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id)
    );
    ''')

    # Return
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Return (
        item_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (item_id, user_id),
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id)
    );
    ''')

    # ========== DONATION ==========

    # Donation
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Donation (
        donation_id INTEGER PRIMARY KEY
    );
    ''')

    # Donated
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Donated (
        item_id INTEGER,
        donation_id INTEGER,
        PRIMARY KEY (item_id, donation_id),
        FOREIGN KEY (item_id) REFERENCES LibraryItems(item_id),
        FOREIGN KEY (donation_id) REFERENCES Donation(donation_id)
    );
    ''')

    # ========== FUTURE ADDITIONS ==========

    # Future Additions
    cur.execute('''
    CREATE TABLE IF NOT EXISTS FutureAdditions (
        future_item_id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT
    );
    ''')

    # Suggests
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Suggests (
        user_id INTEGER,
        future_item_id INTEGER,
        PRIMARY KEY (user_id, future_item_id),
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id),
        FOREIGN KEY (future_item_id) REFERENCES FutureAdditions(future_item_id)
    );
    ''')

    # ========== EVENTS ==========

    # Library Events
    cur.execute('''
    CREATE TABLE IF NOT EXISTS LibraryEvents (
        event_id INTEGER PRIMARY KEY,
        location TEXT,
        title TEXT,
        audience TEXT,
        date TEXT,
        start_time TEXT,
        end_time TEXT
    );
    ''')

    # Attend
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Attend (
        event_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (event_id, user_id),
        FOREIGN KEY (event_id) REFERENCES LibraryEvents(event_id),
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id)
    );
    ''')

    # Member
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Member (
        event_id INTEGER,
        volunteer_id INTEGER,
        PRIMARY KEY (event_id, volunteer_id),
        FOREIGN KEY (event_id) REFERENCES LibraryEvents(event_id),
        FOREIGN KEY (volunteer_id) REFERENCES Volunteer(volunteer_id)
    );
    ''')

    # Registered (BCNF-compliant)
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Registered (
        event_id INTEGER,
        volunteer_id INTEGER,
        PRIMARY KEY (event_id, volunteer_id),
        FOREIGN KEY (event_id) REFERENCES LibraryEvents(event_id),
        FOREIGN KEY (volunteer_id) REFERENCES Volunteer(volunteer_id)
    );
    ''')



    # ========== ROOMS ==========

    # Rooms
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Rooms (
        room_id INTEGER PRIMARY KEY,
        capacity INTEGER,
        floor TEXT
    );
    ''')

    # Social Room
    cur.execute('''
    CREATE TABLE IF NOT EXISTS SocialRoom (
        room_id INTEGER PRIMARY KEY,
        FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
    );
    ''')

    # Hosts
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Hosts (
        room_id INTEGER,
        event_id INTEGER,
        PRIMARY KEY (room_id, event_id),
        FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
        FOREIGN KEY (event_id) REFERENCES LibraryEvents(event_id)
    );
    ''')

    # User Support Tickets
    cur.execute('''
    CREATE TABLE IF NOT EXISTS SupportTickets(
        ticket_id INTEGER PRIMARY KEY,
        personnel_ID INTEGER,
        user_id INTEGER,
        text_info TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES LibraryUsers(user_id),
        FOREIGN KEY (personnel_ID) REFERENCES Personnel(personnel_ID)
    );
    ''')

    # Triggers 

    # ensure we cant borrow books that have no available copies
    cur.execute('''
        CREATE TRIGGER StopBorrow
        BEFORE INSERT ON Borrow
        FOR EACH ROW
        WHEN (SELECT available_copies FROM LibraryItems WHERE item_id = NEW.item_id) <= 0
        BEGIN
            SELECT RAISE(ABORT, 'No available copies');
        END;
    ''')

    # Update available copies for borrowing
    cur.execute('''
        CREATE TRIGGER AvailablePlus
        AFTER INSERT ON Borrow
        FOR EACH ROW
        BEGIN
            UPDATE LibraryItems
            SET available_copies = available_copies - 1
            WHERE (item_id = NEW.item_id);
        END;
    ''')

    # Update available copies for returning
    cur.execute('''
        CREATE TRIGGER AvailableMinus
        BEFORE DELETE ON Borrow
        FOR EACH ROW
        BEGIN
            UPDATE LibraryItems
            SET available_copies = available_copies + 1
            WHERE item_id = OLD.item_id;
        END;
    ''')

    conn.commit()
    return conn