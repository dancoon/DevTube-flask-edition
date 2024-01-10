from application.models import storage
from application.models.users import User


def create_user(name, email, password):
    """Create a new user"""
    user = User()
    user.name = name
    user.email = email
    user.set_password(password)
    user.save()
    return user


def get_user_by_email(email):
    """Get a user by email"""
    try:
        user = storage.get_obj_by_attr("users", {"email": email})
    except Exception as e:
        return None
    return User(**user) if user else None


def get_user_by_id(user_id):
    """Get a user by id"""
    user = storage.get_obj_by_id("users", user_id)
    return User(**user) if user else None


def get_all_users():
    """Get all users"""
    users = storage.get_all("users")
    return [User(**user).to_dict() for user in users]


def update_user(user_id, data):
    """Update a user"""
    update_obj = storage.update_obj("users", user_id, data)
    if update_obj.modified_count == 0:
        raise Exception("Update failed")
    user = get_user_by_id(user_id)
    return user


def delete_user(user_id):
    """Delete a user"""
    delete_obj = storage.delete_obj("users", user_id)
    if delete_obj.deleted_count == 0:
        raise Exception("Delete failed")
    return True
