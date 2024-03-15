# bookstore/bookstore.py
'''class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)'''
import sqlite3

class Bookstore:
    def __init__(self):
        self.conn = sqlite3.connect('bookstore.db')
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books
                     (id INTEGER PRIMARY KEY,
                      title TEXT,
                      author TEXT,
                      price REAL)''')
        self.conn.commit()

    def add_book(self, book):
        c = self.conn.cursor()
        c.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (book.title, book.author, book.price))
        self.conn.commit()

    def get_books(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM books")
        return c.fetchall()

