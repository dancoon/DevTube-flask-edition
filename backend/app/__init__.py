from flask import Flask

from app.routes.auth_routes import configure_oauth
from config import settings


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.Config)
    app.secret_key = app.config.get("SECRET_KEY")
    app.url_map.strict_slashes = False

    configure_oauth(app)

    from app.routes import auth_routes

    app.register_blueprint(auth_routes.auth)

    return app
