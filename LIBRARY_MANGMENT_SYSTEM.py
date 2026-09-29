books = []

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    book = {
        "name": name,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


def display_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("\n--- Book List ---")
        for i in range(len(books)):
            print("Book ID:", i + 1)
            print("Name:", books[i]["name"])
            print("Author:", books[i]["author"])
            print("Status:", books[i]["status"])
            print()


def issue_book():
    display_books()

    if len(books) == 0:
        return

    book_id = int(input("Enter Book ID to issue: "))

    if book_id >= 1 and book_id <= len(books):
        if books[book_id - 1]["status"] == "Available":
            books[book_id - 1]["status"] = "Issued"
            print("Book issued successfully!")
        else:
            print("This book is already issued.")
    else:
        print("Invalid Book ID.")


def return_book():
    display_books()

    if len(books) == 0:
        return

    book_id = int(input("Enter Book ID to return: "))

    if book_id >= 1 and book_id <= len(books):
        if books[book_id - 1]["status"] == "Issued":
            books[book_id - 1]["status"] = "Available"
            print("Book returned successfully!")
        else:
            print("This book is already available.")
    else:
        print("Invalid Book ID.")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")