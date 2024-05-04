class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def print_book(self):
        print(f"{self.title} written by {self.author}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for i in self.books:
            if i.author == book.author and i.title == book.title:                
                self.books.remove(i)
    
    def search_books(self, search_string):
        result = []
        target = search_string.lower()
        for i in self.books:
            if target in i.author.lower() or target in i.title.lower():
                result.append(i)
        return result

    def print_library(self):
        for i in self.books:
            print(f"{i.author} {i.title}")