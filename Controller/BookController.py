from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime

from Model import BookModel, AuthorModel, UserModel, db
from View import book_json, books_json

class BookController(Resource):
    def get(self):
        return books_json.dump(BookModel.query.all() or [])

    def delete(self, id):
        book = BookModel.query.filter(BookModel.id == id).first()
        if book is None:
            return {"message": "Not found book id"}
        db.session.delete(book)

        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}
        return {"message": "Done - Book Deleted"}

    def post(self):
        args = self._add_book_validation()
        
        try:
            authors = AuthorModel.query.filter(AuthorModel.id.in_(args.authors + [2])).all()
            if len(args.authors) != len(authors):
                return {"message": "Author with ID {i} Not found"}
        except SQLAlchemyError as e:
            print(e)
            return {"message": "SQLAlchemyError"}

        user = UserModel.query.filter(UserModel.id == args.posted_by).first()
        if user is None:
            return {"message": "User with ID {i} Not found"}

        book = BookModel(
            id=args.id,
            title=args.title,
            edition=args.edition or "first",
            postedDate= args.postedDate or datetime.now(),
            posted_by=user,
            author=authors
        )   

        db.session.add_all([user, book])
        try:
            db.session.commit()
        except (SQLAlchemyError, IntegrityError) as e:
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "IntegrityError"}
            
        return book_json.dump(book)
        
    def patch(self, id):
        args = self._edit_book_validation()
        
        book = BookModel.query.filter(BookModel.id == id).first()
        if book is None:
            return {"message": "Not found book id"}

        user = None        
        if args.posted_by:
            user = UserModel.query.filter(UserModel.id == args.posted_by).first()
            if user is None:
                return {"message": "Not found user id (posted_by)"}

        authors = None
        if args.author:
            authors = AuthorModel.query.filter(AuthorModel.id.in_(args.author)).all() or []
            if len(authors) != len(args.author):
                return {"message": f"Not found authors IDs"}
 

        book.title = book.title or args.title
        book.posted_by = book.posted_by or user
        book.author = book.author or authors
        book.edition = book.edition or args.edition

        try: 
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(e)
            if type(e) == SQLAlchemyError:
                return {"message": "SQLAlchemyError"}
            return {"message": "SQLAlchemyError"}

        return book_json.dump(book)
        

    def _add_book_validation(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True, help="ID (integer) is required")
        parser.add_argument("title", type=str, required=True, help="title (String) is required")
        parser.add_argument("posted_by", type=int, required=True, help="posted_by a.k.a 'user id' (integer) is required")
        parser.add_argument("author", type=int, action="append", required=True, help="author ID (integer) is required")
        parser.add_argument("edition", type=str, help="edition should be a String")
        parser.add_argument("postedDate", type=str, help="postedDate should be a DateTime")

        return parser.parse_args()



    def _edit_book_validation(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="title should be a integer String")
        parser.add_argument("posted_by", type=int, help="posted_by (user ID) should be a integer")
        parser.add_argument("author", type=int, action="append", help="author (ID) should be a integer")
        parser.add_argument("edition", type=str, help="edition should be a String")

        return parser.parse_args()

    # 1:M
    posted_by = db.relationship("User", backref="posted_books")
    # M:M
    author = db.relationship("Author", secondary="author_book", backref="books")