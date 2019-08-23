from marshmallow import Schema, fields


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()


incoming_book_data = {
    "title": "Clean Code",
    "author": "Bob Martin",
    "description": "A book about writing cleaner code, with examples in Java",
}

book_schema = BookSchema()
book = book_schema.load(incoming_book_data)

print(book)
