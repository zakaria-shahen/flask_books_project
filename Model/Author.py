from Model.DB import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    # M:1
    books = db.relationship("Book.id", backref="author")


