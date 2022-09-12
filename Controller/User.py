from flask_restful import Resource
from Model import User as Data, db
from View import user_json, users_json

class User(Resource):
    def get(self):
        return users_json.dump(Data.query.all() or [])