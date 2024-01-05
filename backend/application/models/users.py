import bcrypt
from bson import ObjectId

from application.models import storage
from application.models.base import BaseModel


class User(BaseModel):
    """User model for storing user-related details"""

    collection = "users"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.name = None
        # self.email = None
        # self.password = None

    def check_password(self, password):
        """Check if password matches"""
        pwd = self.password.encode("utf-8")
        print(pwd)
        return bcrypt.checkpw(password.encode("utf-8"), pwd)

    def set_password(self, password):
        """Set the password for a user"""
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def get_all_users(self):
        """Get all users"""
        queryset = storage.get_all(self.collection)
        print(queryset)
        users = []
        for user in queryset:
            users.append(User(**user).to_dict())
        return users

    def to_dict(self):
        new_dict = super().to_dict()
        if "password" in new_dict:
            del new_dict["password"]
        return new_dict
