from flask_restful import Resource, reqparse
from Model import UserModel, db
from View import user_json, users_json
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class User(Resource):
    
    def get(self, id=None):
        if id is None:
            return users_json.dump(UserModel.query.all() or [])
        return user_json.dump(UserModel.query.filter(UserModel.id == id).first() or [{"status": 404, "message": "user not found"}])

    def delete(self, id):
        print("id", id)
        user = UserModel.query.filter(UserModel.id == id).first()
        if user is None:
            return {"message": "User id not found"}
        db.session.delete(user)
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}
        return {"message": "Done - Deleted user"}

    def patch(self, id):
        args = self._edit_user_validation()
        user = UserModel.query.filter(UserModel.id == id).first()
        if user is None:
            return {"message": "user not found"}
        user.username = args.username or user.username
        user.password = args.password or user.password
        
        try: 
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}

        return user_json.dump(user)

    def post(self):
        args = self._add_user_validation()

        user = UserModel(id=args.id, username=args.username, password=args.password)
        db.session.add(user)
        try:  
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}

        return users_json.dump(UserModel.query.filter(UserModel.id == args.id) or [])
    
    def _add_user_validation(self):
        args = reqparse.RequestParser()
        args.add_argument("id", type=int, help="id (integer) not found ", required=True)
        args.add_argument("username", type=str, help="username (string) not found", required=True)
        args.add_argument("password", type=str, help="password (string) not found", required=True)
        return args.parse_args(strict=True)
    
    def _edit_user_validation(self):
        args = reqparse.RequestParser()
        args.add_argument("username", type=str, help="username (string) not found")
        args.add_argument("password", type=str, help="password (string) not found")
        return args.parse_args(strict=True)