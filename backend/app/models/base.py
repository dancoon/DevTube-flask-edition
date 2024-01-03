from flask_mongoengine import MongoEngine
from mongoengine import Document, connect

db = MongoEngine()


class BaseModel(db.Document):
    meta = {"abstract": True}
