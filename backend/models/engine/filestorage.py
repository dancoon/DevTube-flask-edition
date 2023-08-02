"""
A module that contains the file storage class.
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ File storage class. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id. """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        new_dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects. """
        try:
            with open(self.__file_path, "r") as file:
                new_dict = json.load(file)
            for key, value in new_dict.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects if it’s inside. """
        if obj:
            del self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]
            self.save()
