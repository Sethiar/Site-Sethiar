"""
Code permettant de définir l'accès aux routes concernant les fonctionnalités utilisateur.
"""

from flask import Blueprint

user_bp = Blueprint('user', __name__)

from app.user import routes

