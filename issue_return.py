from db import get_connection
from datetime import datetime

def issue_book(book_id, user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT qty FROM books WHERE id = ?", (book_id,))
    book = cur.fetchone()
    if not book:
        print("❌ Book not found!")
        return
    if book[0] <= 0:
        print("❌ Book out of stock!")
        return

    issue_date = datetime.now().strftime("%Y-%m-%d")
    cur.execute("INSERT INTO issued_books(book_id, user_id, issue_date) VALUES (?, ?, ?)",
                (book_id, user_id, issue_date))
    cur.execute("UPDATE books SET qty = qty - 1 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("📘 Book issued successfully!")

def return_book(issue_id):
    conn = get_connection()
    cur = conn.cursor()
    return_date = datetime.now().strftime("%Y-%m-%d")

    cur.execute("SELECT book_id FROM issued_books WHERE id = ?", (issue_id,))
    issued = cur.fetchone()
    if not issued:
        print("❌ Invalid issue ID!")
        return

    cur.execute("UPDATE issued_books SET return_date = ? WHERE id = ?", (return_date, issue_id))
    cur.execute("UPDATE books SET qty = qty + 1 WHERE id = ?", (issued[0],))
    conn.commit()
    conn.close()
    print("✅ Book returned successfully!")
