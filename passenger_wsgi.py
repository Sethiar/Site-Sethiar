"""
Configuration du fichier passenger_wsgi.py afin de mettre en ligne sur o2switch.
"""

import sys

# Ajout du chemin vers le répertoire du projet pour la recherche de modules
sys.path.insert(0, '/home/lear9104/sethiarworks.sethiar-lefetey.com/Site-Sethiar')

# Importation de l'application Flask à partir de application.py

try:
    from application import application
except Exception as e:
    raise RuntimeError(f"Erreur lors du chargement de l'application Flask : {e}")
