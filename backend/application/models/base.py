from datetime import datetime

from flask import current_app
from pymongo import MongoClient

time = "%Y-%m-%dT%H:%M:%S.%f"
EXCLUDED_ATTRS = ["client", "db", "collection", "__class__"]


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.client = MongoClient(
            "mongodb+srv://dancoon:XI3wurObRcLT8hMb@cluster0.woaed1v.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client.devtube
        if kwargs:
            for key, value in kwargs.items():
                if key not in EXCLUDED_ATTRS:
                    setattr(self, key, value)
            if kwargs.get("_id", None):
                self._id = str(kwargs["_id"])
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
        else:
            self._id = None
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__

        if "_id" in new_dict:
            new_dict["id"] = new_dict.pop("_id")

        for attr in EXCLUDED_ATTRS:
            if attr in new_dict:
                del new_dict[attr]

        return new_dict
