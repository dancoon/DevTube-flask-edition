from authlib.integrations.flask_client import OAuth
from flask import Blueprint, jsonify, redirect, session, url_for, request
import uuid
from authlib.integrations.base_client.errors import OAuthError

auth = Blueprint("auth", __name__, url_prefix="/auth")

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth = OAuth()


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


def generate_nonce():
    """Generate a string for use as a nonce"""
    return str(uuid.uuid4())


def store_nonce_in_session(nonce):
    """Store a nonce in the session"""
    session["nonce"] = nonce


@auth.route("/")
def index():
    return (
        jsonify("Hello " + session["user_name"])
        if "user" in session
        else jsonify("Hello World")
    )


@auth.route("/login")
def login():
    nonce = generate_nonce()
    store_nonce_in_session(nonce)
    redirect_uri = url_for("auth.auth_route", _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)


@auth.route("/authenticate")
def auth_route():
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
    session.pop("user", None)
    return redirect(url_for("auth.index"))
