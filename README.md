# effective_mobile_internship


# Overview 

This application was developed to manage the library of books. There is a database of books, and users can add, delete, display and change the status of books.

# Features

**Add a book** : Add new books to the library with their titles, authors, and publication years. ID part will be incremented with each book addded.
**Delete a book**: Deleted book with provided ID from json file
**Search**: Searchs for the books given title, author name or year of publication. Whitespaces will be trimmed while searching
**Display**: Displays all the books in the database
**Change book status**: Basically changes the status of the book: available or checked out.



## Classes explanation

### `Book`
### Initialization:
- `id`: Unique identifier for the book.
- `title`: Title of the book.
- `author`: Author of the book.
- `year`: Year of publication.
- `status`: Current status of the book (default is "available").

**Methods:**
- `to_dict()`: Converts the book instance to a dictionary for JSON serialization.

### `Library`
Manages a collection of `Book` objects with the following methods:
- `load_books()`: Loads books from a JSON file.
- `save_books()`: Saves the current list of books to a JSON file.
- `add_book(title, author, year)`: Adds a new book to the library.
- `delete_book(book_id)`: Deletes a book from the library by ID.
- `search_books(query)`: Searches for books by title, author, or year.
- `display_books()`: Displays all books in the library.
- `change_status(book_id, new_status)`: Changes the status of a book.

## Usage

1. **Run the Program**: Execute the script to start the Library Management System.

   python library_management.py
   
2. **Choose an Option**: Follow the prompts to select an option:
Add a Book
Delete a Book
Search Books
Display All Books
Change Book Status
Exit the Program



# Requirements
Python 3.x
JSON file for data storage (automatically created if it does not exist)