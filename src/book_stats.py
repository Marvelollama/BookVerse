class BookStats(dict):
    def __init__(self):
        super.__init__()
    
    def track_borrow(self, book):
        self[book] = self.get(book, 0) + 1
        
    def most_borrowed(self):
        if not self:
            return None
        max_borrowed = max(self.values())
        return [book for book, count in self.items() if count == max_borrowed]