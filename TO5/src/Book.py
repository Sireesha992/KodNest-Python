class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)
title = "Atomic Habits"
author = "James clear"
price = 499
book = Book(title, author, price)
print("BOOK DETAILS")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"price: {book.price}")

