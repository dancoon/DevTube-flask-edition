from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    from config import settings

    app = Flask(__name__)
    app.config.from_object(settings.Config)
    app.secret_key = app.config.get("SECRET_KEY")
    app.url_map.strict_slashes = False

    jwt = JWTManager(app)

    from application.routes.auth_routes import configure_oauth

    configure_oauth(app)

    from application.routes import auth_routes, user_routes

    app.register_blueprint(auth_routes.auth)
    app.register_blueprint(user_routes.user)

    return app
