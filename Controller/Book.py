from flask_restful import Resource
from Model import Book as data, db

class Book(Resource):
    def get(self):
        return {"status": True}


