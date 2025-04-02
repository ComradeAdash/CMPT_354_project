import sqlite3

def seed():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # ---------------------
    # Seed LibraryUsers (30 total, 10 are personnel)
    # ---------------------
    users = [(i + 1, f'User{i + 1}', f'user{i + 1}@example.com', f'604-000-{1000 + i}') for i in range(30)]
    cur.executemany("INSERT INTO LibraryUsers VALUES (?, ?, ?, ?);", users)

    # ---------------------
    # Seed Personnel (first 10 users)
    # ---------------------
    personnel = [(i + 1, users[i][1], 'Librarian' if i % 2 == 0 else 'IT') for i in range(10)]
    cur.executemany("INSERT INTO Personnel VALUES (?, ?, ?);", personnel)

    # ---------------------
    # Seed WorksFor
    # ---------------------
    worksFor = [(i + 1, i + 1) for i in range(10)]
    cur.executemany("INSERT INTO WorksFor VALUES (?, ?);", worksFor)

    # ---------------------
    # Seed LibraryItems
    # ---------------------
    items = [(i + 1, (i % 5) + 1, f'Title {i + 1}') for i in range(10)]
    cur.executemany("INSERT INTO LibraryItems VALUES (?, ?, ?);", items)

    # ---------------------
    # Seed BookMetadata
    # ---------------------
    book_metadata = [(f'978-0-{i + 100000000}-{i + 1}', f'Publisher{i + 1}', f'Author{i + 1}') for i in range(10)]
    cur.executemany("INSERT INTO BookMetadata VALUES (?, ?, ?);", book_metadata)

    # ---------------------
    # Seed PrintBooks (5 items)
    # ---------------------
    print_books = [(i + 1, book_metadata[i][0]) for i in range(5)]
    cur.executemany("INSERT INTO PrintBooks VALUES (?, ?);", print_books)

    # ---------------------
    # Seed OnlineBooks (2 items)
    # ---------------------
    online_books = [
        (6, 'http://example.com/book6', book_metadata[5][0]),
        (7, 'http://example.com/book7', book_metadata[6][0])
    ]
    cur.executemany("INSERT INTO OnlineBooks (item_id, url, ISBN) VALUES (?, ?, ?);", online_books)

    # ---------------------
    # Seed Magazines (1 item)
    # ---------------------
    magazines = [(8, '1234-5678')]
    cur.executemany("INSERT INTO Magazines VALUES (?, ?);", magazines)

    # ---------------------
    # Seed MediaMetadata
    # ---------------------
    media_metadata = [
        (1, 'Vinyl', 'Artist1', 'Jazz'),
        (2, 'CD', 'Artist2', 'Pop')
    ]
    cur.executemany("INSERT INTO MediaMetadata VALUES (?, ?, ?, ?);", media_metadata)

    # ---------------------
    # Seed Records
    # ---------------------
    records = [(9, 1)]
    cur.executemany("INSERT INTO Records VALUES (?, ?);", records)

    # ---------------------
    # Seed CDs
    # ---------------------
    cds = [(10, 2)]
    cur.executemany("INSERT INTO CDs (item_id, media_id) VALUES (?, ?);", cds)

    # ---------------------
    # Seed Borrow
    # ---------------------
    borrow = [(i + 1, (i % 10) + 1, (i % 10) + 1, 'borrowed', '2025-04-01', 0.00) for i in range(10)]
    cur.executemany("INSERT INTO Borrow VALUES (?, ?, ?, ?, ?, ?);", borrow)

    # ---------------------
    # Seed LibraryEvents
    # ---------------------
    events = [(i + 1, f'Room {100 + i}', f'Event {i + 1}', 'All Ages', f'2025-04-{10 + i}', '10:00', '12:00') for i in range(10)]
    cur.executemany("INSERT INTO LibraryEvents VALUES (?, ?, ?, ?, ?, ?, ?);", events)

    # ---------------------
    # Seed Volunteers
    # ---------------------
    volunteers = [(i + 1,) for i in range(3)]
    cur.executemany("INSERT INTO Volunteer (volunteer_id) VALUES (?);", volunteers)

    # ---------------------
    # Seed Registered
    # ---------------------
    registered = [(i + 1, i + 1) for i in range(3)]
    cur.executemany("INSERT INTO Registered VALUES (?, ?);", registered)

    conn.commit()
    conn.close()
    print("✅ Dummy data inserted successfully.")