# 📚 Library Management System

A Python-based Library Management System for managing books, searching records, issuing and returning books, and tracking library statistics using CSV storage.

---

# 📌 Overview

A simple command-line application designed to manage library book records with persistent CSV-based storage and a modular Python structure.

---

# ✨ Features

- 📖 Add Book
- 📋 View Books
- 🔍 Search Book
- 📤 Issue Book
- 📥 Return Book
- 🗑️ Delete Book
- 📊 View Library Statistics
- 💾 CSV-based data storage

---

# 🛠️ Technologies Used

- Python 3
- CSV
- File Handling
- Modular Programming
- Command-Line Interface (CLI)

---

# 📁 Project Structure

```text
Library-Management-System/
│
├── main.py
├── ui.py
├── database.py
├── library_books.csv
└── README.md
```

---

# 📖 Workflow

```text
Program Start
      │
      ▼
main.py
      │
      ▼
Load Books
      │
      ▼
Display Menu
      │
      ├── Add Book
      ├── View Books
      ├── Search Book
      ├── Issue Book
      ├── Return Book
      ├── Delete Book
      ├── Show Statistics
      └── Exit
      │
      ▼
Update Book Records
      │
      ▼
Save Data to CSV
```

---

# 🚀 How to Run

### Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### Open the Project

```bash
cd Library-Management-System
```

### Run the Application

```bash
python main.py
```

---

# 🔄 Data Flow

```text
User
 │
 ▼
ui.py
 │
 ▼
database.py
 │
 ▼
library_books.csv
 │
 ▼
Updated Library Records
```

---

# 📂 Module Responsibilities

### `main.py`
- Starts the application
- Loads book records
- Launches the menu

### `ui.py`
- Handles user interaction
- Displays menus, books, and statistics
- Processes library operations

### `database.py`
- Manages book records
- Handles CSV loading and saving
- Performs search and CRUD operations
- Tracks book availability

### `library_books.csv`
- Stores book ID, title, author, genre, and issue status

---

# 🔮 Future Improvements

- 👤 Member Management
- 📅 Due Date Tracking
- 💰 Fine Calculation
- 🔐 Admin Login
- 📊 Advanced Reports
- 🗄️ SQLite/MySQL Integration
- 🖥️ GUI Interface

---

# 👨‍💻 Author

**Swopnil Biswas**

B.Tech – Electronics & Communication Engineering
