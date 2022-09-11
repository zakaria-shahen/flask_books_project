from flask_restful import Resource
from Model import Book as data, db

class User(Resource):
    def get(self):
        return {"s":True}