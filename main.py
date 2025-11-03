import sys, os
sys.path.append(os.path.dirname(__file__))
from db import setup_database
from books import add_book, view_books, update_book, delete_book
from library_user import add_user, view_users
from issue_return import issue_book, return_book

def menu():
    print("\n===== 📚 LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book Quantity")
    print("4. Delete Book")
    print("5. Add User")
    print("6. View Users")
    print("7. Issue Book")
    print("8. Return Book")
    print("0. Exit")
    return input("Enter choice: ")

def main():
    setup_database()
    while True:
        choice = menu()
        if choice == "1":
            add_book(input("Title: "), input("Author: "), int(input("Quantity: ")))
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book(int(input("Book ID: ")), int(input("New Quantity: ")))
        elif choice == "4":
            delete_book(int(input("Book ID: ")))
        elif choice == "5":
            add_user(input("Name: "), input("Email: "))
        elif choice == "6":
            view_users()
        elif choice == "7":
            issue_book(int(input("Book ID: ")), int(input("User ID: ")))
        elif choice == "8":
            return_book(int(input("Issue ID: ")))
        elif choice == "0":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
