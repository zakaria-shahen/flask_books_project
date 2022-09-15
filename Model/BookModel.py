from config import db
# from sqlalchemy.orm import relationship, backref

author_book = db.Table(
    "author_book",
    db.Column("author", db.Integer, db.ForeignKey("author.id"), primary_key=True),
    db.Column("book", db.Integer, db.ForeignKey("book.id"), primary_key=True)
)

class BookModel(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    edition = db.Column(db.String)
    postedDate = db.Column(db.DateTime)
    posted_by_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # 1:M
    posted_by = db.relationship("UserModel", backref="posted_books")
    # M:M
    author = db.relationship("AuthorModel", secondary="author_book", backref="books")


