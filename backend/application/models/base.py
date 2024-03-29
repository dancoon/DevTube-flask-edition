from datetime import datetime

from flask import current_app
from pymongo import MongoClient

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    _id = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if kwargs.get("_id", None):
                self._id = str(kwargs["_id"])
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)

            if kwargs.get("created_at", None) is None:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) is None:
                self.updated_at = datetime.utcnow()
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        return new_dict

    def save(self):
        """save the instance into the database"""
        from application.models import storage

        print(self.to_dict())
        if self._id:
            storage.update_obj(self.collection, self._id, self.to_dict())
        else:
            storage.create_obj(self.collection, self.to_dict())

    def __str__(self) -> str:
        return str(self.to_dict())
