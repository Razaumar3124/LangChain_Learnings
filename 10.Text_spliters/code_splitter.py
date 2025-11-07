from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """


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
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks[0])
