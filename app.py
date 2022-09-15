from config import app, db, json
from Model import BookModel, UserModel, AuthorModel, author_book
from Controller import api

# Database Run
app.app_context().push()
db.drop_all()
db.create_all()

# restful API
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)