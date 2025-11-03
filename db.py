import sqlite3

def get_connection():
    return sqlite3.connect("library.db")

def setup_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        qty INTEGER DEFAULT 1
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS issued_books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user_id INTEGER,
        issue_date TEXT,
        return_date TEXT,
        FOREIGN KEY(book_id) REFERENCES books(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()
