import database as db
import ui


def main():
    db.load_books()
    ui.menu()


if __name__ == "__main__":
    main()