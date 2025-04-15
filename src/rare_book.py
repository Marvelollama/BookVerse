from book import Book

class RareBook(Book):
    def __init__(self, name, author, isbn, copies, condition):
        super().__init__(name, author, isbn, copies)
        self.condition = condition
    
    def __str__(self):
        return super().__str__() + f"and is Rare"
    
    def __add__(self, num):
        print("can't increase copies")
    
    