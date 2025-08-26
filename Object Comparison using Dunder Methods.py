class Book:
    def __init__(self, pages):
        self.pages = pages

    def __lt__(self, other):
        return self.pages < other.pages
    
book1 = Book(200)
book2 = Book(150)
print(book1 < book2)