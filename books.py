from db import get_connection

def add_book(title, author, qty):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO books(title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    conn.commit()
    conn.close()
    print("✅ Book added successfully!")

def view_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    print("\n📚 Books in Library:")
    for r in rows:
        print(f"ID: {r[0]} | Title: {r[1]} | Author: {r[2]} | Quantity: {r[3]}")

def update_book(book_id, qty):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE books SET qty = ? WHERE id = ?", (qty, book_id))
    conn.commit()
    conn.close()
    print("✅ Book quantity updated!")

def delete_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("🗑️ Book deleted!")
