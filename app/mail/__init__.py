"""
Code permettant de définir l'accès aux routes concernant les fonctions de mailing du site.
"""

from flask import Blueprint

mail_bp = Blueprint('mail', __name__)

from app.mail import routes
