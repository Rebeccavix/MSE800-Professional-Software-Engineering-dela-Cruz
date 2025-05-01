# Library Book Manager Using classes
# Task: Manage a small library — add and show books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Added {book} to the library.')

    def show_books(self):
        if self.books:
            print("\nBooks in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("\nThe library is empty.")


# Example usage
library = Library()
library.add_book("Kataraina", "Becky Manawatu")
library.add_book("The Heart in Winter", "Kevin Barry")

library.show_books()

# Output:
# Added "Kataraina" by Becky Manawatu to the library.
# Added "The Heart in Winter" by Kevin Barry to the library.

# Books in the library:
# - "Kataraina" by Becky Manawatu
# - "The Heart in Winter" by Kevin Barry
