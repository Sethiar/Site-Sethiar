"""
Code gérant le bannissement/débannissement des utilisateurs.
"""
from flask_wtf import FlaskForm

from wtforms import HiddenField, SubmitField


# Formulaire permettant de bannir un utilisateur.
class BanUserForm(FlaskForm):
    """
    Formulaire permettant de bannir un utilisateur.

    Attributes :
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.
        submit (SubmitField): Bouton de soumission du formulaire.

    Example:
        form = BanUserForm()

    """

    # Token de sécurité.
    csrf_token = HiddenField()

    # Action de soumettre le formulaire.
    submit = SubmitField('Bannir')


# Formulaire permettant de bannir un utilisateur.
class UnBanUserForm(FlaskForm):
    """
    Formulaire permettant de débannir un utilisateur.

    Attributes :
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.
        submit (SubmitField): Bouton de soumission du formulaire.

    Example:
        form = UnBanUserForm()
    """

    # Token de sécurité.
    csrf_token = HiddenField()

    # Action de soumettre le formulaire.
    submit = SubmitField('Débannir')