books = []
next_id = 1

def add_book():
    global next_id
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    book = {"id": next_id, "title": title, "author": author, "genre": genre, "issued": False}
    books.append(book)
    next_id += 1
    print(f"Book added successfully with ID {book['id']}!\n")

def view_books():
    if not books:
        print("No books available.\n")
        return
    print("\n--- Library Books ---")
    print(f"{'ID':<5}{'Title':<20}{'Author':<15}{'Genre':<12}{'Status':<10}")
    print("-" * 62)
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(f"{book['id']:<5}{book['title'][:19]:<20}{book['author'][:14]:<15}{book['genre'][:11]:<12}{status:<10}")
    print()

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def search_book():
    query = input("Enter title or author to search: ").lower()
    results = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
    if not results:
        print("No matching books found.\n")
        return
    print("\n--- Search Results ---")
    for b in results:
        status = "Issued" if b["issued"] else "Available"
        print(f"{b['id']}. {b['title']} by {b['author']} ({b['genre']}) - {status}")
    print()

def issue_book():
    view_books()
    if not books:
        return
    try:
        book_id = int(input("Enter book ID to issue: "))
    except ValueError:
        print("Invalid input.\n")
        return
    book = find_book(book_id)
    if not book:
        print("Book not found.\n")
    elif book["issued"]:
        print("Book already issued.\n")
    else:
        book["issued"] = True
        print(f"'{book['title']}' issued successfully!\n")

def return_book():
    view_books()
    if not books:
        return
    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Invalid input.\n")
        return
    book = find_book(book_id)
    if not book:
        print("Book not found.\n")
    elif not book["issued"]:
        print("This book was not issued.\n")
    else:
        book["issued"] = False
        print(f"'{book['title']}' returned successfully!\n")

def delete_book():
    view_books()
    if not books:
        return
    try:
        book_id = int(input("Enter book ID to delete: "))
    except ValueError:
        print("Invalid input.\n")
        return
    book = find_book(book_id)
    if not book:
        print("Book not found.\n")
        return
    confirm = input(f"Delete '{book['title']}'? (y/n): ").lower()
    if confirm == "y":
        books.remove(book)
        print("Book deleted successfully.\n")
    else:
        print("Deletion cancelled.\n")

def show_stats():
    total = len(books)
    issued = len([b for b in books if b["issued"]])
    available = total - issued
    print("\n--- Library Statistics ---")
    print(f"Total Books    : {total}")
    print(f"Issued Books   : {issued}")
    print(f"Available Books: {available}\n")

def main():
    while True:
        print("===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Show Statistics")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            show_stats()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

main()