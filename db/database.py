import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="book_db",
        user="admin",
        password="admin1337"
    )