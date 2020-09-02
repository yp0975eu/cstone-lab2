"""
Part 1: Author class
Create a new class called Author
An Author has a name, and a list of books published
When you create a new Author, they don't have any books. So create an empty books list attribute in __init__
Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list
Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles
Write a main function to test your class, create some example authors, and publish some example books
"""

class Author():
    def __init__(self, name):
      self.name = name
      self.books = [] # create empty list 

    def publish(self, bookTitle):
        self.books.append(bookTitle.title())

    def __str__(self):
        return self.name + ' has published: ' + ', '.join(self.books)

a = Author('Branden')
a.publish('the road to demascus')
a.publish('arriving in demascus')
print(a)