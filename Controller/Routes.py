from flask_restful import Api
from Controller import Book, User

api = Api()
# Paths
api.add_resource(Book, "/books")
api.add_resource(User, "/users")