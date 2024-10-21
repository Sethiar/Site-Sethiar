"""
Code permettant de définir l'accès aux routes concernant le chat des utilisateurs du site.
"""

from flask import Blueprint

chat_bp = Blueprint('chat', __name__)

from app.chat import routes

