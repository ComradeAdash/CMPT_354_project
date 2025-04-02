import sqlite3

def seed():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # ---------------------
    # Seed LibraryUsers
    # ---------------------
    users = [
        (1, 'Alice Smith', 'alice@example.com', '604-111-2222'),
        (2, 'Bob Johnson', 'bob@example.com', '604-222-3333'),
        (3, 'Carol Lee', 'carol@example.com', '604-333-4444'),
        (4, 'David Kim', 'david@example.com', '604-444-5555'),
        (5, 'Eva Chan', 'eva@example.com', '604-555-6666'),
        (6, 'Frank Moore', 'frank@example.com', '604-666-7777'),
        (7, 'Grace Wu', 'grace@example.com', '604-777-8888'),
        (8, 'Hannah Patel', 'hannah@example.com', '604-888-9999'),
        (9, 'Ivan Tran', 'ivan@example.com', '604-999-0000'),
        (10, 'Jade Singh', 'jade@example.com', '604-000-1111'),
        (11, 'Kevin Brown', 'kevin@example.com', '604-111-3333'),
        (12, 'Laura Green', 'laura@example.com', '604-222-4444'),
        (13, 'Mike Davis', 'mike@example.com', '604-333-5555'),
        (14, 'Nina White', 'nina@example.com', '604-444-6666'),
        (15, 'Oliver Scott', 'oliver@example.com', '604-555-7777'),
        (16, 'Paula Martinez', 'paula@example.com', '604-666-8888'),
        (17, 'Quinn Nelson', 'quinn@example.com', '604-777-9999'),
        (18, 'Rachel Adams', 'rachel@example.com', '604-888-0000'),
        (19, 'Samuel Carter', 'samuel@example.com', '604-999-1111'),
        (20, 'Tina Evans', 'tina@example.com', '604-000-2222'),
        (21, 'Umar Wilson', 'umar@example.com', '604-111-4444'),
        (22, 'Vera Lopez', 'vera@example.com', '604-222-5555'),
        (23, 'William Harris', 'william@example.com', '604-333-6666'),
        (24, 'Xander Thomas', 'xander@example.com', '604-444-7777'),
        (25, 'Yasmine King', 'yasmine@example.com', '604-555-8888'),
        (26, 'Zachary Hall', 'zachary@example.com', '604-666-9999'),
        (27, 'Amy Turner', 'amy@example.com', '604-777-0000'),
        (28, 'Bryan Parker', 'bryan@example.com', '604-888-1111'),
        (29, 'Chloe Bennett', 'chloe@example.com', '604-999-2222'),
        (30, 'Derek Foster', 'derek@example.com', '604-000-3333')
    ]
    cur.executemany("INSERT INTO LibraryUsers VALUES (?, ?, ?, ?);", users)

    # ---------------------
    # Seed Personnel
    # ---------------------

    personnel = [
        (1, 'Umar Wilson', 'Manager'), 
        (2, 'Vera Lopez', 'Librarian'),
        (3, 'William Harris', 'IT'),
        (4, 'Xander Thomas', 'Librarian'),
        (5, 'Yasmine King', 'IT'),
        (6, 'Zachary Hall', 'Librarian'),
        (7, 'Amy Turner', 'IT'),
        (8, 'Bryan Parker', 'Librarian'),
        (9, 'Chloe Bennett', 'IT'),
        (10, 'Derek Foster', 'Librarian')
    ]
    cur.executemany("INSERT INTO Personnel VALUES (?, ?, ?);", personnel)

    # ---------------------
    # WorksFor
    # ---------------------

    worksFor = [
        (1, 1),  
        (2, 2),  
        (3, 3),  
        (4, 4),  
        (5, 5),  
        (6, 6),  
        (7, 7),  
        (8, 8),  
        (9, 9), 
        (10, 10) 
    ]
    cur.executemany("INSERT INTO WorksFor VALUES (?, ?);", worksFor)

    # ---------------------
    # Seed LibraryItems
    # ---------------------
    items = [
        (1, 3, 'Intro to Databases'),
        (2, 2, 'World History'),
        (3, 5, 'Python Basics'),
        (4, 1, 'Design Patterns'),
        (5, 4, 'Artificial Intelligence'),
        (6, 2, 'Data Structures'),
        (7, 3, 'Modern Art'),
        (8, 1, 'Quantum Physics'),
        (9, 6, 'Digital Photography'),
        (10, 5, 'Ocean Life')
    ]
    cur.executemany("INSERT INTO LibraryItems VALUES (?, ?, ?);", items)

    # ---------------------
    # Seed BookMetadata
    # ---------------------
    book_metadata = [
        ('978-1-11111-111-1', 'O’Reilly', 'Tom White'),
        ('978-1-22222-222-2', 'Penguin', 'Mary Smith'),
        ('978-1-33333-333-3', 'Springer', 'John Doe'),
        ('978-1-44444-444-4', 'No Starch', 'Alice Kim'),
        ('978-1-55555-555-5', 'MIT Press', 'Jane Park'),
    ]
    cur.executemany("INSERT INTO BookMetadata VALUES (?, ?, ?);", book_metadata)

    # ---------------------
    # Seed PrintBooks
    # ---------------------
    print_books = [
        (1, '978-1-11111-111-1'),
        (2, '978-1-22222-222-2'),
        (3, '978-1-33333-333-3'),
        (4, '978-1-44444-444-4'),
        (5, '978-1-55555-555-5')
    ]
    cur.executemany("INSERT INTO PrintBooks VALUES (?, ?);", print_books)

    # ---------------------
    # Seed OnlineBooks
    # ---------------------
    online_books = [
        (6, 'http://example.com/datast', '978-1-11111-111-1'),
        (7, 'http://example.com/modernart', '978-1-22222-222-2')
    ]
    cur.executemany("INSERT INTO OnlineBooks (item_id, url, ISBN) VALUES (?, ?, ?);", online_books)

    # ---------------------
    # Seed Magazines
    # ---------------------
    magazines = [
        (8, '1234-5678')
    ]
    cur.executemany("INSERT INTO Magazines VALUES (?, ?);", magazines)

    # ---------------------
    # Seed MediaMetadata (for CDs and Records)
    # ---------------------
    media_metadata = [
        (1, 'Vinyl', 'Fleetwood Mac', 'Rock'),
        (2, 'CD', 'Taylor Swift', 'Pop')
    ]
    cur.executemany("INSERT INTO MediaMetadata VALUES (?, ?, ?, ?);", media_metadata)

    # ---------------------
    # Seed Records
    # ---------------------
    records = [
        (9, 1)
    ]
    cur.executemany("INSERT INTO Records VALUES (?, ?);", records)

    # ---------------------
    # Seed CDs
    # ---------------------
    cds = [
        (10, 2)
    ]
    cur.executemany("INSERT INTO CDs (item_id, media_id) VALUES (?, ?);", cds)

    # ---------------------
    # Seed Borrow
    # ---------------------
    borrow = [
        (1, 1, 1, 'borrowed', '2025-04-01', 0.00),
        (2, 2, 2, 'borrowed', '2025-04-05', 1.50),
        (3, 3, 3, 'returned', '2025-03-28', 0.00),
        (4, 4, 4, 'borrowed', '2025-04-10', 0.00),
        (5, 5, 5, 'borrowed', '2025-04-02', 0.00),
        (6, 6, 6, 'overdue', '2025-03-20', 3.00),
        (7, 7, 7, 'borrowed', '2025-04-08', 0.00),
        (8, 8, 8, 'returned', '2025-03-25', 0.00),
        (9, 9, 9, 'borrowed', '2025-04-12', 0.00),
        (10, 10, 10, 'borrowed', '2025-04-03', 0.00)
    ]
    cur.executemany("INSERT INTO Borrow VALUES (?, ?, ?, ?, ?, ?);", borrow)

    # ---------------------
    # Seed LibraryEvents
    # ---------------------
    events = [
        (1, 'Room 101', 'Book Club: AI', 'Adults', '2025-04-10', '18:00', '20:00'),
        (2, 'Room 102', 'Art Show', 'All Ages', '2025-04-12', '10:00', '15:00'),
        (3, 'Room 103', 'Poetry Reading', 'Teens', '2025-04-15', '16:00', '18:00')
    ]
    cur.executemany("INSERT INTO LibraryEvents VALUES (?, ?, ?, ?, ?, ?, ?);", events)

    # ---------------------
    # Seed Volunteers and Registered
    # ---------------------
    volunteers = [(1,), (2,), (3,)]
    cur.executemany("INSERT INTO Volunteer (volunteer_id) VALUES (?);", volunteers)

    registered = [(1, 1), (2, 2), (3, 3)]
    cur.executemany("INSERT INTO Registered VALUES (?, ?);", registered)

    conn.commit()
    conn.close()
    print("✅ Dummy data inserted successfully.")