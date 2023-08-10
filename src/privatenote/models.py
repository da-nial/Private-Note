from flask_mongoengine import MongoEngine
from mongoengine import *

db = MongoEngine()


class Note(db.Document):
    unique_url = StringField(primary_key=True, required=True)
    content = StringField(required=True)
    # this field should be filled from config file
    date_expiration = DateTimeField(default=30)

    def __repr__(self) -> str:
        rep_str = "Note: " + self.unique_url + "--- Content: " + self.content
        return rep_str
