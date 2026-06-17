import sqlite3
from datetime import datetime


def save_metadata(file_name, rows_count, columns_count):

    conn = sqlite3.connect("metadata.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datasets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        upload_time TEXT,
        rows_count INTEGER,
        columns_count INTEGER
    )
    """)

    cursor.execute("""
    INSERT INTO datasets
    (file_name, upload_time, rows_count, columns_count)
    VALUES (?, ?, ?, ?)
    """,
    (
        file_name,
        str(datetime.now()),
        rows_count,
        columns_count
    ))

    conn.commit()
    conn.close()