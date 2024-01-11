from application.models import storage
from application.models.base import BaseModel
from application.models.channels import Channel


class Tutor(BaseModel):
    """Tutor model for storing tutor-related details"""

    collection = "tutors"
    username = ""
    approved = False
    channel = Channel()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return f"Tutor: {self.username} - {self.channel_id}"

    def get_all_tutors(self):
        """Get all tutors"""
        queryset = storage.get_all(self.collection)
        tutors = [Tutor(**tutor).to_dict() for tutor in queryset]
        return tutors

    def insert_channel_details(self, channel_details={}):
        """Insert channel details into tutor"""
        self.channel = channel_details
        self.save()

    def get_channel_details(self):
        """Get channel details from tutor"""
        return self.channel.to_dict()

    def get_all_videos(self):
        """Get all videos from tutor"""
        return self.channel.get_all_videos()

    def to_dict(self):
        """Convert object to dictionary"""
        return {"username": self.username, "channel": self.channel.to_dict()}
