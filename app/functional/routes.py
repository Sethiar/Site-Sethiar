"""
Route permettant d'afficher les différentes fonctions légales du site.
"""

from flask import render_template

from app.functional import functional_bp


# Route permettant d'afficher les mentions légales du site.
@functional_bp.route('/mentions-légales')
def mentions():
    """
        Accès aux Mentions légales du site.

        Returns:
            Template HTML de la page de mentions légales du site.
        """
    return render_template("functional/mentions.html")


# Route permettant d'afficher la politique d'utilisation du site.
@functional_bp.route('/politique-de-confidentialité')
def politique():
    """
    Accès à la Politique de confidentialité du site.

    Returns:
        Template HTML de la page de politique de confidentialité du site.
    """
    return render_template("functional/politique.html")

