from config import json as Base
from Model import BookModel

class BookJson(Base.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
    author = Base.HyperlinkRelated("authors", url_key="posted_by_id", external=True)

book_json = BookJson()
books_json = BookJson(many=True)