class Library:
    def __init__(self):
        self.books = []

    def book_inventory(self):
        return len(self.books), self.books

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ID {book_id} not found.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Quantity: {book.quantity}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(
                    f"Found book: ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Quantity: {book.quantity}")
                return
        print(f"Book titled '{title}' not found.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.quantity > 0:
                    book.quantity -= 1
                    print(f"Book '{book.title}' issued. Remaining quantity: {book.quantity}")
                else:
                    print(f"Book '{book.title}' is currently out of stock.")
                return
        print(f"Book with ID {book_id} not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += 1
                print(f"Book '{book.title}' returned. Updated quantity: {book.quantity}")
                return
        print(f"Book with ID {book_id} not found.")