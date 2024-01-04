from bson import ObjectId
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def __init__(self, *args, **kwargs):
        super(CustomJSONEncoder, self).__init__(*args, **kwargs)

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        # Handle other types if needed, e.g., datetime objects
        return super().default(obj)
