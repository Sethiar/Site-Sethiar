"""
Code permettant de définir les routes concernant les fonctions de l'administrateur du site comme, la consultation des
commentaires clients, leur suppression, la gestion des demandes de chat vidéo et l'accès au backend...
"""

from app.admin import admin_bp

from app.Models.admin import Admin

from flask import render_template


# Route permettant de se connecter au backend en tant qu'administrateur.
@admin_bp.route("/backend")
# @admin_required
def backend():
    """
    Affiche la page principale du backend de l'administration.

    Cette route est accessible uniquement aux administrateurs et permet de visualiser la page d'accueil du backend.
    Elle récupère la liste des administrateurs enregistrés et passe ces informations au modèle HTML pour affichage.

    :return: Admin/backend.html
    """
    # Récupération du nom et des informations de l'administrateur.
    admin = Admin.query.all()

    return render_template("Admin/backend.html", admin=admin, logged_in=True)

