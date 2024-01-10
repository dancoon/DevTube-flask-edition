import uuid

from authlib.integrations.base_client.errors import OAuthError
from authlib.integrations.flask_client import OAuth
from flask import Blueprint, jsonify, redirect, request, session, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from application.services.auth_service import AuthService
from application.services.users_services import get_user_by_email

auth = Blueprint("auth", __name__, url_prefix="/auth")

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth = OAuth()
google_auth = AuthService()


def configure_oauth(app):
    """Configure the OAuth instance for the Flask app."""
    oauth.init_app(app)

    oauth.register(
        name="google",
        server_metadata_url=CONF_URL,
        client_kwargs={"scope": "openid email profile"},
        client_id="999851751351-3hnr97ikgj3506o0u72le2d624ed762s.apps.googleusercontent.com",
        client_secret="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",
    )


@auth.route("/")
def index():
    return (
        jsonify("Hello " + session["user_name"])
        if "user" in session
        else jsonify("Hello World")
    )


@auth.route("/google/login")
def login():
    """Redirect the user to the Google OAuth Provider."""
    nonce = google_auth.generate_nonce()
    google_auth.store_nonce_in_session(nonce)
    redirect_uri = url_for("auth.auth_route", _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)


@auth.route("/authenticate")
def auth_route():
    """Authenticate the user with Google OAuth."""
    try:
        nonce = request.args.get("nonce")
        token = oauth.google.authorize_access_token()
        user_info = oauth.google.parse_id_token(token, nonce=nonce)
    except OAuthError as e:
        print(e)
        return jsonify("Error")
    session["user"] = user_info.get("sub")
    session["user_email"] = user_info.get("email")
    session["user_name"] = user_info.get("name")
    return redirect(url_for("auth.index"))


@auth.route("/logout")
def logout():
    """Log the user out of the application."""
    session.pop("user", None)
    return redirect(url_for("auth.index"))


@auth.route("/jwt/create", methods=["POST"])
def jwt_login():
    """Log the user in using a JWT."""
    from application.models.users import User

    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "Missing email or password"})
    try:
        user = get_user_by_email(email)
        if not user:
            return jsonify({"message": "User does not exist"})
        if not user.check_password(password):
            return jsonify({"message": "Incorrect password"})
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    except Exception as e:
        return jsonify({"message": f"Error {e}"})


@auth.route("/jwt/refresh", methods=["POST"])
@jwt_required(refresh=True)
def jwt_refresh():
    """Refresh the JWT token."""
    email = get_jwt_identity()
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200
