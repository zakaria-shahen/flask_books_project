from config import json
from Model import AuthorModel


class AuthorView(json.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel
    

author_view = AuthorView()
authors_view = AuthorView(many=True)