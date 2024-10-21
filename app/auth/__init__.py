"""
Code permettant de définir l'accès aux routes concernant l'authentification des utilisateurs du site.
"""

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from app.auth import routes
