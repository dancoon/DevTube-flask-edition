import bcrypt
from bson import ObjectId

from application.models import storage
from application.models.base import BaseModel


class User(BaseModel):
    """User model for storing user-related details"""

    collection = "users"
    name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_password(self, password):
        """Check if password matches"""
        try:
            pwd = self.password.encode("utf-8")
            print(pwd)
            return bcrypt.checkpw(password.encode("utf-8"), pwd)
        except Exception as e:
            print(e)
            return False

    def set_password(self, password):
        """Set the password for a user"""
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.password = password.decode("utf-8")

    def get_all_users(self):
        """Get all users"""
        queryset = storage.get_all(self.collection)
        users = [User(**user).to_dict() for user in queryset]
        return users
