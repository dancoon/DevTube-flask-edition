from bson import ObjectId
from pymongo import MongoClient


class MongoEngine:
    """MongoEngine class"""

    def __init__(self, *args, **kwargs):
        self.client = MongoClient(
            "mongodb+srv://dancoon:XI3wurObRcLT8hMb@cluster0.woaed1v.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client.devtube

    def get_all(self, collection):
        """Get all documents from a collection"""
        return self.db[collection].find()

    def get_obj_by_id(self, collection, user_id):
        """Get a single document from a collection"""
        try:
            query = {"_id": ObjectId(user_id)}
        except Exception as e:
            raise ValueError(f"Error converting '_id' to ObjectId: {e}")
        return self.db[collection].find_one(query)

    def get_obj_by_attr(self, collection, query):
        """Get a single document from a collection"""
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary type")
        return self.db[collection].find_one(query)

    def create_obj(self, collection, data):
        """Create a new document in a collection"""
        return self.db[collection].insert_one(data)

    def update_obj(self, collection, id, data):
        """Update a document in a collection"""
        return self.db[collection].update_one({"_id": ObjectId(id)}, {"$set": data})

    def delete_obj(self, collection, id):
        """Delete a document from a collection"""
        return self.db[collection].delete_one({"_id": ObjectId(id)})
