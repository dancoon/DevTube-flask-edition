from application.models.base import BaseModel
import bcrypt

class User(BaseModel):
    """User model for storing user related details"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = self.db['users']
        self.name = None
        self.email = None
        self.password = None
    
    def create_user(self, name="", email=None, password=None):
        """Create a new user"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = self({
            'name': name,
            'email': email,
            'password': hashed_password.decode('utf-8')
        })
        res = self.collection.insert_one(user.to_dict())
        user['_id'] = str(res.inserted_id)
        return user
    
    def check_password(self, password):
        """Check if password matches"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def get_user_by_email(self, email):
        """Get a user by email"""
        return self.collection.find_one({'email': email})  # Use to_dict here
    
    def get_user_by_id(self, id):
        """Get a user by id"""
        return self.collection.find_one({'_id': id})  # Use to_dict here

    def get_all_users(self):
        """Get all users"""
        users_cursor = self.collection.find()
        return list(users_cursor)  # Use to_dict here
    
    def update_user(self, id, data):
        """Update a user"""
        return self.collection.update_one({'_id': id}, {'$set': data})
    
    def delete_user(self, id):
        """Delete a user"""
        return self.collection.delete_one({'_id': id})
