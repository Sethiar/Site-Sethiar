"""
Code permettant de définir l'accès aux routes concernant les fonctions administrateur du site.
"""

from flask import Blueprint

admin_bp = Blueprint('Admin', __name__)

from app.admin import routes

