class Book:
    def __init__(self, title, author, isbn, copies): # should i add type hints?
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
    
    def __str__(self):
        return f"{self.title} is written by {self.author} (ISBN: {self.isbn}) ,has {self.copies} left"
    
    def __add__(self, num):
        return Book(self.copies + num)
    
    def __sub__(self, num):
        return Book(self.copies - num)
    