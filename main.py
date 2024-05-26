# Book Store APP
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from google.cloud import firestore

app = FastAPI()

# Initialize Firestore client
db = firestore.Client()


class Book(BaseModel):
    name: str
    category: str


@app.post("/books/")
async def create_book(book: Book):
    doc_ref = db.collection('books').document()
    doc_ref.set(book.dict())
    return {"id": doc_ref.id}


@app.get("/books/")
async def search_books(name: str = Query(None)):
    books = []
    query = db.collection('books')

    if name:
        query = query.where('name', '>=', name).where('name', '<=', name + u'\uf8ff')

    for doc in query.stream():
        books.append(doc.to_dict())

    return books


@app.get("/books/{category}/")
async def list_books_by_category(category: str, preference: str = None):
    books = []
    query = db.collection('books').where('category', '==', category)

    if preference:
        query = query.where('category', '==', category).where('preference', '==', preference)

    for doc in query.stream():
        books.append(doc.to_dict())

    return books

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
