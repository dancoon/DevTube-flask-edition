from flask import jsonify

class UserController:
    """User controller class."""
    def __init__(self):
        from application.models.users import User
        self.object = User()

    def user_details(self, user_id):
        """Get user details."""
        user = self.object.get_user_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        return jsonify(user), 200
    
    def users(self):
        """Get all users."""
        users = self.object.get_all_users()
        print(users)
        return jsonify(users), 200
    
    def create_user(self, data):
        """Create a new user."""
        email = data["email"]
        user = self.object.get_user_by_email(email)
        if user:
            return {"message": "User already exists."}, 400
        user = self.object.create_user(**data)  
        return jsonify(user), 201
    
    def update_user(self, user_id, data):
        """Update a user."""
        user = self.object.get_user_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        user = self.object.update_user(user_id, data)
        return jsonify(user), 200
    
    def delete_user(self, user_id):
        """Delete a user."""
        user = self.object.get_user_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        user = self.object.delete_user(user_id)
        return {"message": "User deleted."}, 200
    