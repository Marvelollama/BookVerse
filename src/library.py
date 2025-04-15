class Library:
    def __init__(self):
        self.books = dict()
        self.members = dict()
        
    def add_book(self, book):
        self.books[book.isbn] = book
    
    def remove_book(self, book):
        del self.books[book.isbn]
        
    def register_member(self, member):
        self.members[member.id] = member
        
    def search_book(self, book):
        if book.isbn in self.books:
            return self.books[book.isbn]
        else:
            print(f"{book.title} is unavailable")
    
    def __getitem__(self, isbn):
        return self.books.get(isbn, None)
    