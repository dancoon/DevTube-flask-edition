from flask import Flask

from application.routes.auth_routes import configure_oauth
from config import settings


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.Config)
    app.secret_key = app.config.get("SECRET_KEY")
    app.url_map.strict_slashes = False

    configure_oauth(app)


    try:
        client.admin.command("ping")
        print("Connected to MongoDB")
    except Exception as ex:
        print("Could not connect to MongoDB: ", ex)


    from application.routes import auth_routes
    from application.routes import user_routes

    app.register_blueprint(auth_routes.auth)
    app.register_blueprint(user_routes.user)

    return app