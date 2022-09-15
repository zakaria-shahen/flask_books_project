from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from Model import AuthorModel, db
from View import author_view, authors_view

class AuthorController(Resource):
    def get(self, id=None):
        if id is None:
            return authors_view.dump(AuthorModel.query.all() or [])
        return authors_view.dump(AuthorModel.query.filter(AuthorModel.id == id).all() or [])

    def post(self):
        args = self._add_author_validation()
        author = AuthorModel(id=args.id, name=args.name)
        db.session.add(author)
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}

        return author_view.dump(author)

    def patch(self, id):
        args = self._edit_author_validation()

        author =  AuthorModel.query.filter(AuthorModel.id == id).first()
        if author is None:
            return {"message": "Author ID not Found"}

        author.name = args.name or author.name
        
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}

        return author_view.dump(author)
        
    def delete(self, id):
        author =  AuthorModel.query.filter(AuthorModel.id == id).first()
        if author is None:
            return {"message": "Author ID not Found"}
        db.session.delete(author)
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}
        return {"message": "Done - Author Deleted"}

    def _add_author_validation(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help="ID (integer) is required")
        parser.add_argument('name', type=str, required=True, help="name (string) is required")
        return parser.parse_args()
    
    def _edit_author_validation(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="name should be a String")
        return parser.parse_args()