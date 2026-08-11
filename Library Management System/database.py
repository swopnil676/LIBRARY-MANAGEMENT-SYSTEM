import csv
import os

CSV_FILE = "library_books.csv"
FIELDS = ["id", "title", "author", "genre", "issued"]

books = []
next_id = 1


def load_books():
    global books, next_id
    if not os.path.exists(CSV_FILE):
        return
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append({
                "id": int(row["id"]),
                "title": row["title"],
                "author": row["author"],
                "genre": row["genre"],
                "issued": row["issued"].lower() == "true"
            })
    if books:
        next_id = max(b["id"] for b in books) + 1


def save_books():
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for b in books:
            writer.writerow(b)


def add_book(title, author, genre):
    global next_id
    book = {"id": next_id, "title": title, "author": author, "genre": genre, "issued": False}
    books.append(book)
    next_id += 1
    save_books()
    return book


def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def search_books(query):
    query = query.lower()
    return [b for b in books if query in b["title"].lower() or query in b["author"].lower()]


def delete_book(book):
    books.remove(book)
    save_books()


def get_stats():
    total = len(books)
    issued = len([b for b in books if b["issued"]])
    return total, issued, total - issued