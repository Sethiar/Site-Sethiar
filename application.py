"""
Configuration du fichier application.py sert pour mise en ligne sur o2switch.
"""

import sys
from app import create_app

# Ajout du chemin vers le dossier de l'application
sys.path.insert(0, '/home/lear9104/sethiarworks.sethiar-lefetey.com/Site-Sethiar')

# Création de l'application Flask
app = create_app()

# Expose l'application comme instance WSGI pour Passenger
application = app
