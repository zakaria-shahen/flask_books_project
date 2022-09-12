from .Main import json as Base
import Model

class UserJson(Base.Schema):
    class Meta:
        fields = ("id", "username")
    _link = Base.Hyperlinks({
        "self": Base.URLFor("users", value=dict(id="<id>")),
        "collection": Base.URLFor("users")
    })


user_json = UserJson()
users_json = UserJson(many=True)