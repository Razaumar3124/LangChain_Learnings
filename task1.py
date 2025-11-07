import random
from datetime import datetime

class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrower = None
        self.borrow_date = None

    def borrow(self, borrower_name):
        """Marks the book as borrowed by a user."""
        if self.is_borrowed:
            print(f"❌ '{self.title}' is already borrowed by {self.borrower}.")
        else:
            self.is_borrowed = True
            self.borrower = borrower_name
            self.borrow_date = datetime.now().strftime("%d-%m-%Y %H:%M")
            print(f"📚 '{self.title}' borrowed successfully by {borrower_name}.")

    def return_book(self):
        """Marks the book as returned."""
        if not self.is_borrowed:
            print(f"⚠️ '{self.title}' is not borrowed.")
        else:
            print(f"✅ '{self.title}' returned by {self.borrower}.")
            self.is_borrowed = False
            self.borrower = None
            self.borrow_date = None


class Library:
    """Represents a collection of books with various operations."""

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        """Adds a new book to the library."""
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"📖 Added '{title}' by {author} to {self.name} library.")

    def show_books(self):
        """Displays all books with their status."""
        if not self.books:
            print("No books in the library yet!")
            return
        print(f"\n📚 Books available in {self.name}:")
        for i, book in enumerate(self.books, 1):
            status = "Available ✅" if not book.is_borrowed else f"Borrowed by {book.borrower} ⏰"
            print(f"{i}. {book.title} by {book.author} — {status}")
        print()

    def random_recommendation(self):
        """Randomly recommends a book."""
        if not self.books:
            print("No books available for recommendation.")
            return
        book = random.choice(self.books)
        print(f"💡 Book Recommendation: '{book.title}' by {book.author}")


# -------------------- Outside Class Functions --------------------
def welcome_message():
    print("=" * 40)
    print("📚 Welcome to the Python Library System 📚")
    print("=" * 40)

def main():
    welcome_message()
    my_library = Library("City Central")

    # Add some books
    my_library.add_book("The Alchemist", "Paulo Coelho")
    my_library.add_book("1984", "George Orwell")
    my_library.add_book("Clean Code", "Robert C. Martin")

    # Show all books
    my_library.show_books()

    # Borrow a random book
    random_book = random.choice(my_library.books)
    random_book.borrow("Abdurrazzak")

    # Show books again after borrowing
    my_library.show_books()

    # Return the borrowed book
    random_book.return_book()

    # Show final list
    my_library.show_books()

    # Recommend a random book
    my_library.random_recommendation()


if __name__ == "__main__":
    main()
