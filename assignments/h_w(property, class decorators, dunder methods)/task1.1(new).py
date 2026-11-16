# AI log: none
# оновлений варіант Task5a з доданими __str__ та __repr__
class Library:
    def __init__(self, name):
        self.name = name
        self.books = set()
        self.authors = set()

    def add_new_book(self, book):
        for book_ex in self.books:
            if book_ex.name == book.name and book_ex.author == book.author:
                raise ValueError("This book already exists in the library")

        self.books.add(book)
        self.authors.add(book.author)

    def group_by_author(self, author):
        new_books = []
        for book in self.books:
            if book.author == author:
                new_books.append(book)
        return new_books

    def group_by_year(self, year):
        new_books = []
        for book in self.books:
            if book.year == year:
                new_books.append(book)
        return new_books



class Author:
    def __init__(self, name,country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = set()

    def write_new_book(self, name, year):
        new_book = Book(name, year, self)
        self.books.add(new_book)
        return new_book


class Book:
    books_count = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        Book.books_count += 1

    def __str__(self):
        return f"{self.name} ({self.year})"


    def __repr__(self):
        return f"Book('{self.name}', {self.year}, author='{self.author.name}')"


library = Library("My Library")
author = Author("Joanne Rowling", "UK", "1965-07-31")

book1 = author.write_new_book("Harry Potter", 1997)
book2 = author.write_new_book("Fantastic Beasts", 2001)
library.add_new_book(book1)
library.add_new_book(book2)

print(book1)
print(repr(book1))

same_book = Book("Harry Potter", 1997, author)
