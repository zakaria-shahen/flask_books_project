from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Model import Book, User, Author, author_book, db
from Controller import api
from View import json

# Flask Config
app = Flask(__name__)

# database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.app_context().push()
db.drop_all()
db.create_all()

# restful API
api.init_app(app)

# Marshmallow
json.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)