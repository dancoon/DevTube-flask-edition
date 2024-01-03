import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "your_secret_key"
    # SQLALCHEMY_DATABASE_URI = 'your_database_uri'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    MONGODB_SETTINGS = {
        'db': 'devtube',
        'host': 'localhost',
        'port': 27017,
        'username': 'devtube',
        'password': 'devtube_pwd'
    }
    
