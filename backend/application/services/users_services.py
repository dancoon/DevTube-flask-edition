from application.models import storage
from application.models.users import User


def create_user(name, email, password):
    """Create a new user"""
    user = User()
    user.name = name
    user.email = email
    user.password = password
    user.save()
    return user


def get_user_by_email(email):
    """Get a user by email"""
    try:
        user = storage.get_obj_by_attr("users", {"email": email})
        u = User(**user)
        print(u.email)
    except Exception as e:
        print(e)
        return None
    return User(**user)


def get_user_by_id(user_id):
    """Get a user by id"""
    user = storage.get_obj_by_attr("users", {"_id": user_id})
    return user


def get_all_users():
    """Get all users"""
    users = storage.get_all("users")
    return [User(**user).to_dict() for user in users]
