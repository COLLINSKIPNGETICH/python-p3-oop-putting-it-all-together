#!/usr/bin/env python3

# book.py

class Book:
    def __init__(self, title, page_count, price):  # Add the 'price' parameter
        self.title = title
        self.page_count = page_count
        self.price = price  # Set the 'price' attribute
        self.current_page = 1  # Initialize current_page attribute

    def turn_page(self):
        self.current_page += 1
        return "Flipping the page...wow, you read fast!"

    
        