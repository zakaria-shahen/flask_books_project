from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Model import Book, User, Author, author_book, db
from View import api

# Flask Config
app = Flask(__name__)

# database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)
app.app_context().push()
db.create_all()

# restful API
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)