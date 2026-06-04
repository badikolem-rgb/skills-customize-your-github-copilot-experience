from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)

books = [
    Book(id=1, title="The FastAPI Guide", author="Jamie Example", year=2024),
    Book(id=2, title="Python Web APIs", author="Alex Sample", year=2025),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Book Collection API"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    for existing in books:
        if existing.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    return book

@app.get("/search", response_model=List[Book])
def search_books(author: Optional[str] = None):
    if not author:
        return books
    matches = [book for book in books if author.lower() in book.author.lower()]
    return matches
