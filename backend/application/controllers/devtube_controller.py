from flask import jsonify, request

from application.services.devtube_service import create_tutor, get_tutor_by_username


class DevTubeController:
    """Controller for DevTube routes."""

    def __init__(self) -> None:
        """Initialize DevTube controller."""
        from application.models.tutors import Tutor

        self.object = Tutor()

    def tutors(self):
        """Get all tutors."""
        if request.method == "POST":
            data = request.json
            return self.create_tutor(username=data["username"])
        else:
            tutors = self.object.get_all_tutors()
            return jsonify(tutors), 200

    def create_tutor(self, username):
        """Create a new tutor."""
        tutor = get_tutor_by_username(username)
        if tutor:
            return {"message": "Tutor already exists."}, 400
        tutor = create_tutor(username)
        return jsonify(tutor.to_dict()), 201
