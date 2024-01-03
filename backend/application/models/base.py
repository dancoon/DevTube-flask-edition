from flask import current_app
from pymongo import MongoClient

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.client = MongoClient("mongodb+srv://dancoon:XI3wurObRcLT8hMb@cluster0.woaed1v.mongodb.net/?retryWrites=true&w=majority"
)
        self.db = self.client.devtube
        self._id = None
        self.created_at = None
        self.updated_at = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """Convert the object to a dictionary"""
        dictionary = self.__dict__
        dictionary.pop("client")
        dictionary.pop("db")
        dictionary["_id"] = str(dictionary["_id"]) if "_id" in dictionary else None
        dictionary["created_at"] = str(dictionary["created_at"]) if "created_at" in dictionary else None
        dictionary["updated_at"] = str(dictionary["updated_at"]) if "updated_at" in dictionary else None
        return dictionary
