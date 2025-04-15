class Member:
    def __init__(self, name):
        _id_counter = 1
        self.name = name
        self._id_counter = _id_counter
        _id_counter += 1
        self.borrowed_books = []
        
    def __str__(self):
        return f"{self.name} (ID: {self._id_counter}) has borrowed {self.borrowed_books}"
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{book.title} has been borrowed by {self.name}")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")
