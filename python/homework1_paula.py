from random import randint
__author__ = 'Paula'


class AbstractBook(object):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "%s, %s" % (self.title, self.author)


class Book(AbstractBook):

    def __init__(self, title, author, isbn=None, status="available"):
        super(Book, self).__init__(title, author)
        self.status = status

    def update_status(self, status):
        self.status = status


class Person(object):

    def __init__(self, name):
        self.name = name

    def borrow(self, title, isbn=None):
        if isbn is None:
            Inventory.borrow(title=title)
        else:
            Inventory.borrow(isbn=isbn)


class Inventory(object):
    books = {}

    def __init__(self):
        pass

    @classmethod
    def add_book(cls, book):
        parent = Inventory.get_parent(book.title, book.author)
        if parent is None:
            parent = AbstractBook(book.title, book.author)
        Inventory.books[parent] = []
        if type(book) is Book:
            book.status = "available"
            Inventory.books[parent].append(book)

    @classmethod
    def get_parent(cls, title, author):
        for book in Inventory.books:
            if book.author == author and book.title == title:
                return book
        return None

    @classmethod
    def search(cls, title=None, author=None):
        if title is not None and author is not None:
            for ab_book in Inventory.books:
                if ab_book.title == title and ab_book.author == author:
                    return ab_book
        return False

    @classmethod
    def update_status(cls, title, author, status):
        if status == "available":
            other_status = "loan"
        elif status == "loan":
            other_status = "available"
        else:
            print "invalid status"
            return -1
        parent = Inventory.get_parent(title, author)
        if parent is None:
            print "sorry, we do not have the book"
        # elif len(Inventory[parent]) == 0:
        #     print "we have the book but not right now"
        else:
            for book in Inventory.books[parent]:
                if book.status == other_status:
                    book.update_status(status)
                    return 0
        return -1


if __name__ == "__main__":
    b1 = Book("t1", "a1")
    b2 = Book("t2", "a2")
    print Inventory.books
    print "add books that do not exist in the list"
    Inventory.add_book(b1)
    Inventory.add_book(b2)
    for ab_book in Inventory.books:
        print ab_book
        for book in Inventory.books[ab_book]:
            print book.title, book.author, book.status
    print "add book to existing book"
    b11 = Book("t1", "a1")
    Inventory.add_book(b11)
    for ab_book in Inventory.books:
        print ab_book
        for book in Inventory.books[ab_book]:
            print book.title, book.author, book.status
    print "add abstract book that do not exist in the list"
    b3 = AbstractBook("t3", "a3")
    Inventory.add_book(b3)
    for ab_book in Inventory.books:
        print ab_book
        for book in Inventory.books[ab_book]:
            print book.title, book.author, book.status
    print "change status of a1 t1"
    Inventory.update_status("t1", "a1", "loan")
    for ab_book in Inventory.books:
        print ab_book
        for book in Inventory.books[ab_book]:
            print book.title, book.author, book.status
