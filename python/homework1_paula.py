__author__ = 'Paula'

books = {}

def add(title, author, *args, **kwargs):
    global books

    if title not in books:
        books[title] = {}
        books[title]['author'] = author
    if 'copies' not in books[title]:
        books[title]['copies'] = list(args)
    else:
        books[title]['copies'] = books[title]['copies']+ list(args)
    books[title]['no'] = len(books[title]['copies'])


def update_status(title, copy, status):
    global books
    books[title]['copies'][copy] = status


def delete(title, *args, **kwargs):
    global books
    if len(kwargs) == 0:
        books.pop(title)
    else:
        for kw in kwargs:
            books[title]['copies'].pop(kw)


def afisare():
    global books
    print "---"
    for book in books:
        print book, books[book]


def search(word=None, author=None):
    global books
    if author is not None:
        found = False
        for book in books:
            if books[book]['author'] == author:
                print book
                found = True
        if not found:
            print "no book with the requested author"
    if word is not None:
        found = False
        for book in books:
            if books[book].find(word) != -1:
                print book
                found = True
        if not found:
            print "no books containing the required string"


if __name__ == "__main__":
    add("title1", "author1", "loan", "loan", "available")
    add("title2", "author2", "available")
    add("title3", "author3", "available", "available")
    add("title22", "author2", "available", "available")
    afisare()
    update_status("title1", 1, "author1")
    afisare()
    add("title1", "author1", "loan")
    afisare()
    delete("title1")
    afisare()
    print "--"
    search(author="author2")
