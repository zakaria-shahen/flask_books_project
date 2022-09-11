from Model.DB import db
author_book = db.Table(
    "author_book",
    db.Column("author", db.Integer, db.ForeignKey("author.id"), primary_key=True),
    db.Column("book", db.Integer, db.ForeignKey("book.id"), primary_key=True)
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    edition = db.Column(db.String)
    postedDate = db.Column(db.DateTime)
    # M:M
    author = db.relationship("Author", secondary=author_book, backref="book")
    # 1:M
    posted_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


