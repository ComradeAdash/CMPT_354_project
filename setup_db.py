## THIS CREATES THE DATABASE SCHEMA !!
from modules.db import get_db_connection

conn = get_db_connection()
print("Database schema created successfully.")
conn.close()