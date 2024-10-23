"""
Code permettant de définir l'accès aux routes concernant les fonctions administrateur du site.
"""

from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

from app.admin import routes

