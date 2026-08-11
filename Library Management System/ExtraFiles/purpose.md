# Library Management System

A simple CLI-based library management system built in Python with CSV persistence.

## Features

- Add, view, search, issue, return, and delete books
- Persistent storage via `library_books.csv`
- Live statistics (total, issued, available)
- Auto-clearing screen for a clean CLI experience

## Project Structure

```
library-management-system/
├── main.py              # Entry point
├── database.py          # Book model, CSV load/save, CRUD logic
├── ui.py                # CLI menu and user interaction
└── library_books.csv    # Persisted book data
```

## Requirements

- Python 3.7+
- No external dependencies (uses built-in `csv` and `os` modules)

## Usage

```bash
python main.py
```

Follow the on-screen menu:

```
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Show Statistics
8. Exit
```

## Data Format

`library_books.csv` columns:

| Column | Type | Description              |
|--------|------|---------------------------|
| id     | int  | Unique book ID             |
| title  | str  | Book title                 |
| author | str  | Author name                |
| genre  | str  | Book genre                 |
| issued | bool | Whether the book is issued |

## Notes

- If `library_books.csv` doesn't exist, it's created automatically on first save.
- IDs auto-increment based on the highest existing ID in the CSV.