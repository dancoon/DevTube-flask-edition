from flask import Blueprint, jsonify, request

from application.controllers.users_controller import UserController

user = Blueprint("user", __name__, url_prefix="/users")

controller = UserController()


@user.route("/<user_id>", methods=["GET"])
def user_details(user_id):
    """Get user details."""
    return controller.user_details(user_id)


@user.route("/", methods=["GET"])
def users():
    """Get all users."""
    return controller.users()


@user.route("/", methods=["POST"])
def create_user():
    """Create a new user."""
    data = request.get_json()
    return controller.create_user(data)


# @user.route("/<user_id>", methods=["PUT"])
# def update_user(user_id):
#     """Update a user."""
#     data = request.get_json()
#     return controller.update_user(user_id, data)


# @user.route("/<user_id>", methods=["DELETE"])
# def delete_user(user_id):
#     """Delete a user."""
#     return controller.delete_user(user_id)
