#!/usr/bin/env python3
"""
Library Management System module - Basic OOP implementation
"""


class Book:
    """
    Book class with public attributes for title and author,
    and a private attribute to track checkout status.
    """
    def __init__(self, title, author):
        """
        Initialize a new Book instance.

        Args:
            title: The title of the book (string)
            author: The author of the book (string)
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Check out this book if it's available.
        
        Returns:
            bool: True if checkout was successful, False if already checked out
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Return this book if it's checked out.
        
        Returns:
            bool: True if return was successful, False if not checked out
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def __str__(self):
        """
        Return a string representation of the book.
        """
        status = "checked out" if self._is_checked_out else "available"
        return f"'{self.title}' by {self.author} ({status})"


class Library:
    """
    Library class that manages a collection of books.
    """
    def __init__(self):
        """
        Initialize a new Library instance with an empty books list.
        """
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book: A Book instance to add to the library
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book from the library by title.

        Args:
            title: The title of the book to check out

        Returns:
            bool: True if the book was checked out successfully, False otherwise
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return a book to the library by title.

        Args:
            title: The title of the book to return

        Returns:
            bool: True if the book was returned successfully, False otherwise
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """
        List all available books in the library.

        Returns:
            list: A list of Book instances that are available for checkout
        """
        available_books = [book for book in self._books if not book._is_checked_out]
        
        for book in available_books:
            print(f"{book.title} by {book.author}")
        
        return available_books
