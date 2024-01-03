import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "your_secret_key"
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    MONGO_URI = "mongodb+srv://dancoon:XI3wurObRcLT8hMb@cluster0.woaed1v.mongodb.net/?retryWrites=true&w=majority"
