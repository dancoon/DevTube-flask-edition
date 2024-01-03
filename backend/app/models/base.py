from mongoengine import connect
from mongoengine import connect, Document
from flask_mongoengine import MongoEngine


db = MongoEngine()

class BaseModel(db.Document):
    meta = {'abstract': True}
    