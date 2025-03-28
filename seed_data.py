import sqlite3
## THIS POPULATES TABLES WITH DATA !!
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
    ]
    cur.executemany("INSERT INTO LibraryUsers VALUES (?, ?, ?, ?);", users)

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
    # Seed PrintBooks (item_id = FK)
    # ---------------------
    print_books = [
        (1, '978-1-11111-111-1', 'O’Reilly', 'Tom White'),
        (2, '978-1-22222-222-2', 'Penguin', 'Mary Smith'),
        (3, '978-1-33333-333-3', 'Springer', 'John Doe'),
        (4, '978-1-44444-444-4', 'No Starch', 'Alice Kim'),
        (5, '978-1-55555-555-5', 'MIT Press', 'Jane Park'),
        (6, '978-1-66666-666-6', 'O’Reilly', 'Lucas Tan'),
        (7, '978-1-77777-777-7', 'Penguin', 'Mei Lin'),
        (8, '978-1-88888-888-8', 'Wiley', 'Derek Sun'),
        (9, '978-1-99999-999-9', 'Springer', 'Nora Hall'),
        (10, '978-1-10101-010-1', 'O’Reilly', 'George King')
    ]
    cur.executemany("INSERT INTO PrintBooks VALUES (?, ?, ?, ?);", print_books)

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
        (4, 'Room 104', 'Film Night', 'Adults', '2025-04-17', '19:00', '21:00'),
        (5, 'Room 105', 'History Lecture', 'Seniors', '2025-04-20', '14:00', '16:00'),
        (6, 'Room 106', 'Coding for Kids', 'Children', '2025-04-22', '13:00', '15:00'),
        (7, 'Room 107', 'Music Jam', 'All Ages', '2025-04-24', '17:00', '19:00'),
        (8, 'Room 108', 'Local Author Talk', 'Adults', '2025-04-26', '18:00', '19:30'),
        (9, 'Room 109', 'Photography Basics', 'Teens', '2025-04-28', '16:30', '18:30'),
        (10, 'Room 110', 'Kids Storytime', 'Children', '2025-04-30', '10:00', '11:00'),
    ]
    cur.executemany("INSERT INTO LibraryEvents VALUES (?, ?, ?, ?, ?, ?, ?);", events)

    conn.commit()
    conn.close()
    print("Dummy data inserted successfully.")

# Run the seeder
seed()
