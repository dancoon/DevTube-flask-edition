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

    def get_obj_by_attr(self, collection, query):
        """Get a single document from a collection"""
        print(self.db[collection].find_one({"_id": ObjectId("6597e97eba06d7ea78c20348")}))
        return self.db[collection].find_one({"_id": ObjectId(query["_id"])})

    def create_obj(self, collection, data):
        """Create a new document in a collection"""
        return self.db[collection].insert_one(data)

    def update_obj(self, collection, id, data):
        """Update a document in a collection"""
        return self.db[collection].update_one({"_id": id}, {"$set": data})

    def delete_obj(self, collection, id):
        """Delete a document from a collection"""
        return self.db[collection].delete_one({"_id": id})
