from fastapi import APIRouter, HTTPException
from dao.book_dao import BookDAO
from db.schemas import Book

router = APIRouter()
book_dao = BookDAO()

@router.get("/books/")
def read_books():
    return book_dao.get_books()

@router.post("/books/", status_code=201)
def add_book(book: Book):
    new_book = book_dao.add_book(book)
    return new_book

@router.put("/books/{book_id}/", status_code=200)
def update_book(book_id: int, book: Book):
    updated_book = book_dao.update_book(book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/books/{book_id}/", status_code=200)
def delete_book(book_id: int):
    deleted = book_dao.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

