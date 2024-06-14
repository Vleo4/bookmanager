from psycopg2.extras import RealDictCursor
from db.database import get_db_connection


class BookDAO:
    def __init__(self):
        self.conn = get_db_connection()

    def get_books(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM books")
            return cursor.fetchall()

    def add_book(self, book):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "INSERT INTO books (title, author, published_year, genre) VALUES (%s, %s, %s, %s) RETURNING id, title, author, published_year, genre",
                (book.title, book.author, book.published_year, book.genre))
            new_book = cursor.fetchone()
            self.conn.commit()
            return new_book

    def update_book(self, book_id, book):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""
                UPDATE books SET title=%s, author=%s, published_year=%s, genre=%s 
                WHERE id=%s RETURNING id, title, author, published_year, genre
            """, (book.title, book.author, book.published_year, book.genre, book_id))
            updated_book = cursor.fetchone()
            self.conn.commit()
            return updated_book

    def delete_book(self, book_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM books WHERE id=%s RETURNING id", (book_id,))
            self.conn.commit()
            return cursor.rowcount > 0