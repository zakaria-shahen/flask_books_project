from Model.DB import db
from Model.Book import Book

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    # M:1
    books = db.relationship("Book", secondary="author_book", back_populates='author')


