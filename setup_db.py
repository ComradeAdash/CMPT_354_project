# reset_db.py
import sqlite3
import os
from modules.db import get_db_connection
from modules.seed_data import seed

DB_FILE = 'library.db'

# Step 1: Delete old database file
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"Deleted existing {DB_FILE}.")

# Step 2: Rebuild schema from db.py (assumes get_db_connection is imported)
conn = get_db_connection()
conn.close()
print("Created BCNF-compliant schema.")

# Step 3: Seed fresh data
seed()
