from authlib.integrations.flask_client import OAuth
from flask import Blueprint, jsonify, redirect, session, url_for, request
import uuid

auth = Blueprint("auth", __name__, url_prefix="/auth")

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth = OAuth()

def configure_oauth(app):
    # Initialize the OAuth instance with the Flask app
    oauth.init_app(app)

    oauth.register(
        name="google",
        server_metadata_url=CONF_URL,
        client_kwargs={"scope": "openid email profile"},
        client_id="999851751351-3hnr97ikgj3506o0u72le2d624ed762s.apps.googleusercontent.com",
        client_secret="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",
    )

# Function to generate a unique nonce (you may use a more sophisticated method)
def generate_nonce():
    return str(uuid.uuid4())

# Function to store the nonce in the session
def store_nonce_in_session(nonce):
    session['nonce'] = nonce

@auth.route("/")
def index():
    if "user" in session:
        return jsonify("Hello " + session["user_name"])
    return jsonify("Hello World")

@auth.route("/login")
def login():
    nonce = generate_nonce()
    store_nonce_in_session(nonce)
    redirect_uri = url_for("auth.auth_route", _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)

@auth.route("/authenticate")
def auth_route():
    nonce = request.args.get('nonce')
    token = oauth.google.authorize_access_token()
    user_info = oauth.google.parse_id_token(token, nonce=nonce)
    session["user"] = user_info.get("sub")
    session["user_email"] = user_info.get("email")
    session["user_name"] = user_info.get("name")
    return redirect(url_for("auth.index"))

@auth.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("auth.index"))
