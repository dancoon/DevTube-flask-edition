"""
A module that contains the user class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class. """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ User class constructor. """
        super().__init__(*args, **kwargs)
