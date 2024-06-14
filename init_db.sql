CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_year INTEGER NOT NULL,
    genre VARCHAR(100) NOT NULL
);

INSERT INTO books (title, author, published_year, genre) VALUES
('1984', 'George Orwell', 1949, 'Dystopian'),
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Historical Fiction');