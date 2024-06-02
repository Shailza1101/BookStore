from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# In-memory data store for books (replace with a database in production)
books_db = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Store API"}

@app.post("/books/")
def create_book(book: dict):
    """
    Create a new book entry.

    Parameters:
    - book (dict): The book data to be added.

    Returns:
    - dict: A response message indicating success or failure.
    """
    isbn = book["isbn"]
    if isbn in books_db:
        return {"message": "Book with the same ISBN already exists"}
    books_db[isbn] = book
    return {"message": "Book created successfully"}


@app.get("/books/{isbn}")
def read_book(isbn: str):
    """
    Retrieve book details by ISBN.

    Parameters:
    - isbn (str): The ISBN of the book to retrieve.

    Returns:
    - dict: The book details or a message if the book is not found.
    """
    if isbn in books_db:
        return books_db[isbn]
    return {"message": "Book not found"}

@app.put("/books/{isbn}")
def update_book(isbn: str, updated_book: dict):
    """
    Update book information by ISBN.

    Parameters:
    - isbn (str): The ISBN of the book to update.
    - updated_book (dict): The updated book data.

    Returns:
    - dict: A response message indicating success or failure.
    """
    if isbn in books_db:
        books_db[isbn] = updated_book
        return {"message": f"Updated book with ISBN: {isbn}"}
    return {"message": "Book not found"}


@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    """
    Delete a book by ISBN.

    Parameters:
    - isbn (str): The ISBN of the book to delete.

    Returns:
    - dict: A response message indicating success or failure.
    """
    if isbn in books_db:
        del books_db[isbn]
        return {"message": f"Deleted book with ISBN: {isbn}"}
    return {"message": "Book not found"}
