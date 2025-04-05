class Book:
    count = 0

    def __init__(self):
        Book.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

book1 = Book()

print(book1)

print(book1.get_count())