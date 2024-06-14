import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from dao.book_dao import BookDAO
from db.schemas import Book

@pytest.fixture
def client():
    return TestClient(app)

@patch('dao.book_dao.BookDAO', autospec=True)
def test_read_books(mock_dao, client):
    # Mocking the DAO methods
    mock_dao.get_books.return_value = [
        Book(id=1, title="Test Book 1", author="Author 1", published_year=2000, genre="Fiction"),
        Book(id=2, title="Test Book 2", author="Author 2", published_year=2000, genre="Fiction"),
    ]

    response = client.get("/books/")
    assert response.status_code == 200

@patch('dao.book_dao.BookDAO', autospec=True)
def test_add_book(mock_dao, client):
    # Mocking the DAO methods
    new_book_data = {"title": "New Book", "author": "New Author", "published_year": 2020, "genre": "Sci-Fi"}
    mock_dao.add_book.return_value = Book(id=3, **new_book_data)

    response = client.post("/books/", json=new_book_data)
    assert response.status_code == 201

@patch('dao.book_dao.BookDAO', autospec=True)
def test_update_book(mock_dao, client):
    # Mocking the DAO methods
    updated_book_data = {"title": "Updated Book", "author": "Updated Author", "published_year": 2015, "genre": "Mystery"}
    mock_dao.update_book.return_value = Book(id=1, **updated_book_data)

    response = client.put("/books/1/", json=updated_book_data)
    assert response.status_code == 200

@patch('dao.book_dao.BookDAO', autospec=True)
def test_delete_book(mock_dao, client):
    # Mocking the DAO methods
    mock_dao.delete_book.return_value = True

    response = client.delete("/books/1/")
    assert response.status_code == 200
