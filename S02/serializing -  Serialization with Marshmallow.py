from marshmallow import Schema, fields


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Clean Code", "Bob Martin")

book_schema = BookSchema()
book_dict = book_schema.dump(book)

print(book_dict)
