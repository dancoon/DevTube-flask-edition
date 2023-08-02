"""
A module that contains the base model class.
"""
from datetime import datetime
import models
import uuid


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Base model class. """
    def __init__(self, *args, **kwargs):
        """ Base model constructor. """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs.keys():
                self.created_at = datetime.now()
            if "updated_at" not in kwargs.keys():
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Base model string representation. """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Base model save method. """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Base model dictionary representation. """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.strftime(time_format)
        new_dict["updated_at"] = self.updated_at.strftime(time_format)
        return new_dict

    def delete(self):
        """ Base model delete method. """
        models.storage.delete(self)
