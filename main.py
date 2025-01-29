# FastAPI Backend (main.py)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    stock: int

# Database simulation
books_db = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", price=9.99, stock=10),
    Book(id=2, title="1984", author="George Orwell", price=12.99, stock=15),
    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", price=14.99, stock=8),
]

# API endpoints
@app.get("/books/", response_model=List[Book])
async def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = next((book for book in books_db if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    if any(b.id == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return book

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)



