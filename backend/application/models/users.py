from bson import ObjectId
from application.models.base import BaseModel
import bcrypt

class User(BaseModel):
    """User model for storing user-related details"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = self.db['users']
        
    
    def create_user(self, name="", email=None, password=None):
        """Create a new user"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {
            'name': name,
            'email': email,
            'password': hashed_password.decode('utf-8')
        }
        res = self.collection.insert_one(user_data)
        user_data['_id'] = str(res.inserted_id)
        return User(**user_data).to_dict()
    
    def check_password(self, password):
        """Check if password matches"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def get_user_by_email(self, email):
        """Get a user by email"""
        data = self.collection.find_one({'email': email})
        return User(data).to_dict() if data else None
    
    def get_user_by_id(self, id):
        """Get a user by id"""
        data = self.collection.find_one({'_id': ObjectId(id)})
        print(User(**data).to_dict())
        return User(**data).to_dict() if data else {}

    def get_all_users(self):
        """Get all users"""
        users_cursor = self.collection.find()
        return [User(**user).to_dict() for user in users_cursor]
    
    def update_user(self, id, data):
        """Update a user"""
        return self.collection.update_one({'_id': id}, {'$set': data})
    
    def delete_user(self, id):
        """Delete a user"""
        return self.collection.delete_one({'_id': id})
