from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Book  # Import the Book model

# Create an instance of FastAPI
app = FastAPI()

# In-memory data store for books (replace with a database in production)
books_db = {}

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    # FastAPI automatically validates the incoming 'book' data
    # If the data is invalid, FastAPI will return a detailed error response
    # If the data is valid, you can proceed to save it
    books_db[book.isbn] = book
    return book

@app.get("/books/{isbn}", response_model=Book)
def read_book(isbn: str):
    # Fetch book data from your data store
    book_data = books_db.get(isbn)
    if book_data is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_data

@app.put("/books/{isbn}", response_model=Book)
def update_book(isbn: str, updated_book: Book):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[isbn] = updated_book
    return updated_book

@app.delete("/books/{isbn}", response_model=Book)
def delete_book(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books_db.pop(isbn)
    return deleted_book