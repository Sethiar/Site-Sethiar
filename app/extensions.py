"""
Code source qui permet d'initialiser les extensions.
"""

import os
import requests

from dotenv import load_dotenv

# Chargement des variables d'environnement depuis .env.
load_dotenv()

# Fonctions vérifiant les extensions des imports.
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx'}


def allowed_file(filename):
    """
    Vérifie si l'extension d'un fichier est autorisée en fonction de la liste ALLOWED_EXTENSIONS.

    :param filename: Nom du fichier à vérifier.

    :return: True si l'extension est autorisée, False sinon.
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

