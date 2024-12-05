import json
import os


class Book:
    """Class to represent a book in the library."""

    def __init__(self, book_id, title, author, year, status="available"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Convert book to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }


class Library:
    """Class to manage the library of books."""

    def __init__(self, filename='data.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Load books from JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(data['id'], data['title'], data['author'], data['year'], data['status']) for data in
                              books_data]

    def save_books(self):
        """Save books to file."""
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)




    def add_book(self, title, author, year):
        """Add a new book to the library."""
        book_id = len(self.books) + 1
        new_book = Book(book_id, title.strip(), author.strip(), year)
        self.books.append(new_book)
        self.save_books()
        print(f'Book "{title.strip()}" added with ID: {book_id}')



    def delete_book(self, book_id):
        """Delete a book from the library by ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f'Book with ID: {book_id} deleted.')
                return
        print(f'Error: Book with ID {book_id} not found.')

    def search_books(self, query):
        """Search for books by title, author, or year."""
        query = query.strip()
        results = [book for book in self.books if (
                query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query == str(book.year)
        )]
        return results

    def display_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books available.")
            return

        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Year':<5} {'Status':<12}")
        print("=" * 80)
        for book in self.books:
            print(f"{book.id:<5} {book.title:<30} {book.author:<20} {book.year:<5} {book.status:<12}")



    def change_status(self, book_id, new_status):
        """Change the status of a book."""
        for book in self.books:
            if book.id == book_id:
                if new_status in ["available", "checked out"]:
                    book.status = new_status
                    self.save_books()
                    print(f'Book ID {book_id} status changed to "{new_status}".')
                else:
                    print('Error: Status must be "available" or "checked out".')
                return
        print(f'Error: Book with ID {book_id} not found.')


# Command line interface

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Change Book Status")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter year of publication: ").strip()
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Enter book ID to delete: ").strip())
            library.delete_book(book_id)
        elif choice == '3':
            query = input("Enter title, or author, or year to search: ").strip()
            results = library.search_books(query)
            if results:
                print(f"Found {len(results)} result(s):")
                for book in results:
                    print(f"{book.title} by {book.author} (ID: {book.id})")
            else:
                print("Could not find any results.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Enter book ID to change status: ").strip())
            new_status = input("Enter new status (available/checked out): ").strip()
            library.change_status(book_id, new_status)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Enter a number less than 6")




if __name__ == "__main__":
    main()
