""" Authentication service"""
import uuid
from flask import session, url_for


class AuthService:
    """Auth service class"""

    def generate_nonce(self):
        """Generate a string for use as a nonce"""
        return str(uuid.uuid4())

    def store_nonce_in_session(self, nonce):
        """Store a nonce in the session"""
        session["nonce"] = nonce

    def login_user(self, oauth):
        """Login user"""
        nonce = self.generate_nonce()
        self.store_nonce_in_session(nonce)
        redirect_uri = url_for("auth.auth_route", _external=True)
        return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)

