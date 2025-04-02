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
        # Original 10
        (1, 3, 'Intro to Databases'),
        (2, 2, 'World History'),
        (3, 5, 'Python Basics'),
        (4, 1, 'Design Patterns'),
        (5, 4, 'Artificial Intelligence'),
        (6, 2, 'Data Structures'),
        (7, 3, 'Modern Art'),
        (8, 1, 'Quantum Physics'),
        (9, 6, 'Digital Photography'),
        (10, 5, 'Ocean Life'),

        # PrintBooks
        (11, 2, 'Neverwhere'),
        (12, 3, 'Animal Farm'),
        (13, 4, 'The Cursed Child'),
        (14, 2, 'The Dark Tower'),
        (15, 1, 'Throne of Glass'),

        # OnlineBooks
        (16, 5, 'Neverwhere Online'),
        (17, 4, 'Animal Farm Online'),
        (18, 3, 'The Cursed Child Online'),
        (19, 2, 'The Dark Tower Online'),
        (20, 1, 'Throne of Glass Online'),

        # Magazines
        (21, 1, 'Global Science'),
        (22, 1, 'Tech Monthly'),
        (23, 1, 'Art Review'),
        (24, 1, 'History Today'),
        (25, 1, 'Kids Corner'),

        # CDs
        (26, 2, 'Adele Greatest Hits'),
        (27, 3, 'Drake Essentials'),
        (28, 4, 'DAMN. by Kendrick'),
        (29, 5, 'Ariana Grande Live'),
        (30, 2, 'Lorde Mood'),

        # Records
        (31, 1, 'The Beatles Classics'),
        (32, 2, 'Beyoncé Platinum'),
        (33, 3, 'Radiohead Mix'),
        (34, 4, 'Vinyl Vibes'),
        (35, 1, 'Jazz Fusion')
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
        ('978-1-66666-105-5', 'HarperCollins', 'Neil Gaiman'),
        ('978-1-66666-106-6', 'Random House', 'George Orwell'),
        ('978-1-66666-107-7', 'Scholastic', 'J.K. Rowling'),
        ('978-1-66666-108-8', 'Simon & Schuster', 'Stephen King'),
        ('978-1-66666-109-9', 'Bloomsbury', 'Sarah J. Maas')
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
        (5, '978-1-55555-555-5'),
        (11, '978-1-66666-105-5'),
        (12, '978-1-66666-106-6'),
        (13, '978-1-66666-107-7'),
        (14, '978-1-66666-108-8'),
        (15, '978-1-66666-109-9')
    ]

    cur.executemany("INSERT INTO PrintBooks VALUES (?, ?);", print_books)

    # ---------------------
    # Seed OnlineBooks
    # ---------------------
    online_books = [
        (6, 'http://example.com/datast', '978-1-11111-111-1'),                  # Data Structures
        (7, 'http://example.com/modernart', '978-1-22222-222-2'),              # Modern Art

        (16, 'http://example.com/neverwhere', '978-1-66666-105-5'),            # Neverwhere Online
        (17, 'http://example.com/animalfarm', '978-1-66666-106-6'),            # Animal Farm Online
        (18, 'http://example.com/cursedchild', '978-1-66666-107-7'),           # The Cursed Child Online
        (19, 'http://example.com/darktower', '978-1-66666-108-8'),             # The Dark Tower Online
        (20, 'http://example.com/throneofglass', '978-1-66666-109-9'),         # Throne of Glass Online

        (28, 'http://example.com/neverwhere', '978-1-66666-105-5'),            # Reused (ok if duplicates allowed)
        (29, 'http://example.com/animalfarm', '978-1-66666-106-6'),
        (30, 'http://example.com/cursedchild', '978-1-66666-107-7'),
        (31, 'http://example.com/darktower', '978-1-66666-108-8'),
        (32, 'http://example.com/throneofglass', '978-1-66666-109-9')
    ]


    cur.executemany("INSERT INTO OnlineBooks (item_id, url, ISBN) VALUES (?, ?, ?);", online_books)

    # ---------------------
    # Seed Magazines
    # ---------------------
    magazines = [
        (8, '1234-5678'),
        (19, '2345-6789'),
        (20, '3456-7890'),
        (21, '4567-8901'),
        (22, '5678-9012'),
        (23, '6789-0123'),
        (24, '7890-1234'),
        (25, '8901-2345'),
        (26, '9012-3456'),
        (27, '0123-4567')
    ]

    cur.executemany("INSERT INTO Magazines VALUES (?, ?);", magazines)

    # ---------------------
    # Seed MediaMetadata (for CDs and Records)
    # ---------------------
    media_metadata = [
        (1, 'Vinyl', 'Fleetwood Mac', 'Rock'),       # Digital Photography (9)
        (2, 'CD', 'Taylor Swift', 'Pop'),            # Ocean Life (10)
        (3, 'CD', 'Adele', 'Soul'),                  # History Today (24)
        (4, 'Vinyl', 'The Beatles', 'Rock'),         # The Beatles Classics (31)
        (5, 'CD', 'Drake', 'Hip-Hop'),               # Kids Corner (25)
        (6, 'Vinyl', 'Beyoncé', 'R&B'),              # Beyoncé Platinum (32)
        (7, 'CD', 'Kendrick Lamar', 'Rap'),          # DAMN. by Kendrick (28)
        (8, 'Vinyl', 'Radiohead', 'Alternative'),    # Radiohead Mix (33)
        (9, 'CD', 'Ariana Grande', 'Pop'),           # Ariana Grande Live (29)
        (10, 'Vinyl', 'Lorde', 'Indie'),             # Lorde Mood (30)
        (11, 'Vinyl', 'Various Artists', 'Jazz')     # Jazz Fusion (35)
    ]



    cur.executemany("INSERT INTO MediaMetadata VALUES (?, ?, ?, ?);", media_metadata)

    # ---------------------
    # Seed Records
    # ---------------------
    records = [
        (9, 1),     # Digital Photography
        (21, 6),    # Global Science
        (22, 8),    # Tech Monthly
        (23, 10),   # Art Review
        (31, 4),    # The Beatles Classics
        (32, 6),    # Beyoncé Platinum
        (33, 8),    # Radiohead Mix
        (34, 10),   # Vinyl Vibes
        (35, 11)    # Jazz Fusion
    ]

    cur.executemany("INSERT INTO Records VALUES (?, ?);", records)

    # ---------------------
    # Seed CDs
    # ---------------------
    cds = [
        (10, 2),   # Ocean Life → Taylor Swift
        (24, 3),   # History Today → Adele
        (25, 5),   # Kids Corner → Drake
        (26, 7),   # Adele Greatest Hits → Kendrick Lamar
        (27, 9),   # Drake Essentials → Ariana Grande
        (28, 7),   # DAMN. by Kendrick → Kendrick Lamar
        (29, 9),   # Ariana Grande Live → Ariana Grande
        (30, 10)   # Lorde Mood → Lorde
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
        (3, 'Room 103', 'Poetry Reading', 'Teens', '2025-04-15', '16:00', '18:00'),
        (4, 'Room 104', 'Game Night', 'Teens', '2025-04-20', '17:00', '21:00'),
        (5, 'Room 105', 'Science Fair', 'Kids', '2025-04-22', '13:00', '16:00'),
        (6, 'Room 106', 'Coding Workshop', 'Adults', '2025-04-25', '14:00', '17:00'),
        (7, 'Room 107', 'Storytelling Hour', 'Kids', '2025-04-28', '11:00', '12:00'),
        (8, 'Room 108', 'Film Screening', 'All Ages', '2025-05-01', '18:00', '20:30'),
        (9, 'Room 109', 'Career Panel', 'Adults', '2025-05-03', '15:00', '17:00'),
        (10, 'Room 110', 'Music Night', 'All Ages', '2025-05-05', '19:00', '21:00')
    ]
    cur.executemany("INSERT INTO LibraryEvents VALUES (?, ?, ?, ?, ?, ?, ?);", events)

    # ---------------------
    # Seed Volunteers and Registered
    # ---------------------
    volunteers = [(1,), (2,), (3,)]
    cur.executemany("INSERT INTO Volunteer (volunteer_id) VALUES (?);", volunteers)

    registered = [(1, 1), (2, 2), (3, 3)]
    cur.executemany("INSERT INTO Registered VALUES (?, ?);", registered)

    # ---------------------
    media_metadata_fixes = [
        (12, 'Vinyl', 'Various Artists', 'Science'),   # Global Science (21)
        (13, 'Vinyl', 'Various Artists', 'Tech'),      # Tech Monthly (22)
        (14, 'Vinyl', 'Various Artists', 'Art'),       # Art Review (23)
        (15, 'CD', 'Various Artists', 'History'),      # History Today (24)
        (16, 'CD', 'Various Artists', 'Kids'),         # Kids Corner (25)
        (17, 'CD', 'Adele', 'Soul'),                   # Adele Greatest Hits (26)
        (18, 'CD', 'Drake', 'Hip-Hop')                 # Drake Essentials (27)
    ]
    cur.executemany("INSERT INTO MediaMetadata VALUES (?, ?, ?, ?);", media_metadata_fixes)

    # CDs
    cds_fixes = [
        (24, 15),  # History Today
        (25, 16),  # Kids Corner
        (26, 17),  # Adele Greatest Hits
        (27, 18)   # Drake Essentials
    ]
    cur.executemany("UPDATE CDs SET media_id = ? WHERE item_id = ?;", [(m[1], m[0]) for m in cds_fixes])

    # Records
    records_fixes = [
        (21, 12),  # Global Science
        (22, 13),  # Tech Monthly
        (23, 14)   # Art Review
    ]
    cur.executemany("UPDATE Records SET media_id = ? WHERE item_id = ?;", [(m[1], m[0]) for m in records_fixes])

    conn.commit()
    conn.close()
    print("✅ Dummy data inserted successfully.")