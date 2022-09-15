from config import db

class AuthorModel(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)


