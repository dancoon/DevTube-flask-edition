def create_tutor(username):
    """Create a new tutor."""
    from application.models import storage
    from application.models.channels import Channel
    from application.models.tutors import Tutor

    tutor = Tutor(username=username, channel=Channel())
    tutor.save()
    return tutor


def get_tutor_by_username(username):
    """Get tutor by username."""
    from application.models import storage
    from application.models.tutors import Tutor

    try:
        tutor = storage.get_obj_by_attr(Tutor.collection, {"username": username})
    except Exception as e:
        return None
    return Tutor(**tutor) if tutor else None
