from db import get_connection

def add_user(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users(name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    print("✅ User added successfully!")

def view_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    print("\n👥 Registered Users:")
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]} | Email: {r[2]}")
