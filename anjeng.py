import os

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Borrowed: {self.is_borrowed}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def remove_book(self, isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book removed: {book_to_remove.title}")
        else:
            print("Book not found")

    def list_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed: {book.title}")
                return
        print("Book not available for borrowing")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned: {book.title}")
                return
        print("Book not found or was not borrowed")

    def save_library(self, filename):
        with open(filename, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.isbn},{book.is_borrowed}\n")
        print("Library saved to file")

    def load_library(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.books = []
                for line in file:
                    title, author, isbn, is_borrowed = line.strip().split(',')
                    book = Book(title, author, isbn)
                    book.is_borrowed = is_borrowed == 'True'
                    self.books.append(book)
            print("Library loaded from file")
        else:
            print("File not found")

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Save Library")
        print("7. Load Library")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)
        elif choice == '5':
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)
        elif choice == '6':
            filename = input("Enter filename to save library: ")
            library.save_library(filename)
        elif choice == '7':
            filename = input("Enter filename to load library: ")
            library.load_library(filename)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
