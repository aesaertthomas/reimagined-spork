# Ex01
# Test class Book
from model.Book import Book

print("\n*******Create a new book*******")
b1 = Book("Python for dummies", "Louis Kegels", "Arco", "125-875-5455")

print(f"Title of book 1: {b1.title}")
b1.title = "Python for dummies bis"
print("Full info book 1")
print(b1)

#create a second book with the students
print("\n*******Create a new book*******")
b2 = Book("How can I find a nice pub in Kortrijk?",
          "Johan Vannieuwenhuyse", "Aveve", "987-875-5455", 2016)
print("Full info book 2")
print(b2)
