from config import json as Base
from Model import UserModel


class UserJson(Base.SQLAlchemySchema):
    class Meta:
        model = UserModel
    id = Base.auto_field()
    username = Base.auto_field()
    # TODO: add  links with ID
    # posted_books = Base.HyperlinkRelated("book", url_key="posted_books", external=True)
    # posted_books = Base.URLFor("book", values=dict(id="<id>"))

user_json = UserJson()
users_json = UserJson(many=True)