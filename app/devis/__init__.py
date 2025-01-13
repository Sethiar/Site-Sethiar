"""
Code permettant de définir l'accès aux routes concernant les fonctions des devis du site.
"""

from flask import Blueprint

devis_bp = Blueprint('devis', __name__)

from app.devis import routes
