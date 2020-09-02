"""
Part 2: Author class - no duplicate books
Start with the program from part 1.
In this version, an author can't publish two books with the same name.
When the publish function is called, print an error message if the book given has the same name as a book currently in the books list. 
"""

class Author():
    def __init__(self, name):
        self.name = name
        self.books = [] # create empty list 

    def publish(self, bookTitle):
        book = bookTitle.title()
        if book in self.books:
            print(f"Sorry, {book} has been published already")
        else:
          self.books.append(book)

    def __str__(self):
        return f"{self.name} has published: {', '.join(self.books)}."

a = Author("Branden")
a.publish("the road to demascus")
a.publish("arriving in demascus")
a.publish("arriving in demascus")
print(a)