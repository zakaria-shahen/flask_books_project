from flask_restful import Api
from Controller import BookController, User, AuthorController

api = Api()

# Paths

""""
    # User Operation 
    ADD user: DELETE /users/<id>
    Edit user: PATCH /users/<id> { <props>, ... }
    get all user: GET /users/
    get one user: GET /users/<id>
    add user: POST /users/<id>
"""
api.add_resource(User, "/users", "/users/<int:id>")



"""
    # author Operation 
    ADD author: DELETE /authors/<id>
    Edit author: PATCH /authors/<id> { <props>, ... }
    get all authors: GET /authors/
    get one author: GET /authors/<id>
    add author: POST /authors/<id>
"""
api.add_resource(AuthorController.AuthorController, "/authors", "/authors/<int:id>", endpoint="authors")



"""
    # Book Operation 
    ADD book: DELETE /books/<id>
    Edit book: PATCH /books/<id> { <props>, ... }
    get all books: GET /books/
    get one book: GET /books/<id>
    add book: POST /books/<id>
"""
api.add_resource(BookController, "/books", "/books/<int:id>", endpoint="books")