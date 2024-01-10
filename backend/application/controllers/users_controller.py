from flask import jsonify

from application.services.users_services import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_email,
    get_user_by_id,
    update_user,
)


class UserController:
    """User controller class."""

    def __init__(self):
        from application.models.users import User

        self.object = User()

    def user_details(self, user_id):
        """Get user details."""
        user = get_user_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        return jsonify(user.to_dict()), 200

    def users(self):
        """Get all users."""
        users = get_all_users()
        return jsonify(users), 200

    def create_user(self, data):
        """Create a new user."""
        email = data["email"]
        user = get_user_by_email(email)
        if user:
            return {"message": "User already exists."}, 400
        user = create_user(
            name=data["name"], email=data["email"], password=data["password"]
        )
        return jsonify(user.to_dict()), 201

    def update_user(self, user_id, data):
        """Update a user."""
        user = get_user_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        try:
            user = update_user(user_id, data)
        except Exception as e:
            return {"message": f"Error {e}"}, 400
        return jsonify(user.to_dict()), 200

    def delete_user(self, user_id):
        """Delete a user."""
        user = get_user_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        try:
            deleted = delete_user(user_id)
        except Exception as e:
            return {"message": f"Error {e}"}, 400
        message = f"{user} deleted" if deleted else f"Error deleting {user}"
        return jsonify({"message": message}), 200
