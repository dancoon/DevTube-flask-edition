"""
A module that contains the tutor class.
"""
from models.base_model import BaseModel


class Tutor(BaseModel):
    """ Tutor class. """
    name = ""
    channel_name = ""
    category = ""

    def __init__(self, *args, **kwargs):
        """ Tutor class constructor. """
        super().__init__(*args, **kwargs)
