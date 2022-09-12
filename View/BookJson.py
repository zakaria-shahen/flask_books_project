from .Main import json as Base

class BookJson(Base.Schema):
    class Meta:
        fields = ("id", "username")
    _link = Base.Hyperlinks({
        "self": Base.URLFor("books", value=dict(id="<id>")),
        "collection": Base.URLFor("books")
    })    