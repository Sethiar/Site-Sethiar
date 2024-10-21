"""
Code permettant de définir l'accès aux routes concernant les fonctions administratives du site.
"""

from flask import Blueprint

frontend_bp = Blueprint('frontend', __name__)

from app.frontend import routes

