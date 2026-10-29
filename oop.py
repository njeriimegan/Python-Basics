class Book:
    # constructor == function
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
    def print_details(self):
        print("Title", self.title)
        print("Author", self.author)
        print("Price", self.price)
        print("-----------------")
    def apply_discount(self, discount):
        self.price = self.price * (1 - discount/100)
        print("New price is ", self.price)

b1 = Book("The Bait of Satan ", "John Bevere", "978-16211365488", 1000)
b1.print_details()
b1.apply_discount(10)

b2 = Book("Maximize Your Potential", "Myles Munroe", "1560439076", 800)
b2.print_details()
print(b2.price)

