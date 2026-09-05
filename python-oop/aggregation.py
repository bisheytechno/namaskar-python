

# class Laptop:
#    def __init__(self,brand):
#       self.brand = brand

#    def code(self):
#       print(f"{self.brand} ma coding gardai xu")

# class Student :
#    def __init__(self,name,laptop):
#       self.name = name
#       self.laptop = laptop

#    def study(self):
#       print(f"Ma {self.name} padhdai xu")
#       self.laptop.code()


# laptop1 = Laptop("DELL")

# student1 = Student("Bishal", laptop1)

# student1.study()

# del student1
# print(laptop1.brand) 


class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
 
    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author} "for book in self.books]

 
class Book :
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("New York Public Library")

book1 =  Book("Harry Potter...", "J.K. Rowling")
book2 =  Book("The Hobbit", "J.R.R Tolkin")
book3 =  Book("The color of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_books():
    print(book)