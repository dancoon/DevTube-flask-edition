from flask import Blueprint, jsonify, request

from application.controllers.devtube_controller import DevTubeController

devtube = Blueprint("devtube", __name__, url_prefix="")

controller = DevTubeController()


@devtube.route("/tutors", methods=["GET", "POST"])
def channels():
    """Get all channels."""
    return controller.tutors()


# @devtube.route("/tutors/<tutor_id>", methods=["GET"])
# def channel_details(tutor_id):
#     """Get channel details."""
#     return controller.tutor_details(tutor_id)

# @devtube.route("/tutors/<tutor_id>/videos", methods=["GET"])
# def videos(tutor_id):
#     """Get all videos."""
#     return controller.videos(tutor_id)
