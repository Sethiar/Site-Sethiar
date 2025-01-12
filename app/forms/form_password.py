"""
Code des formulaires qui permettent de réinitialiser le mot de passe.
"""

from flask_wtf import FlaskForm

from flask_wtf.file import DataRequired

from wtforms import EmailField, PasswordField, SubmitField, HiddenField
from wtforms.validators import EqualTo


# Formulaire pour mot de passe oublié.
class ForgetPassword(FlaskForm):
    """
    Formulaire permettant de réinitialiser le mot de passe.

    Attributes :
        email(EmailField) : Email de l'utilisateur voulant réinitialiser son mot de passe.
        new_password (PasswordField) : Nouveau mot de passe.
        csrf_token (HiddenFields) : Jeton CSRF pour la sécurité du formulaire.
    """

    email = EmailField(
        "Email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Entrez votre email"}
    )

    # Action de soumettre le formulaire.
    submit = SubmitField('Réinitialiser le mot de passe.')

    # Token de sécurité.
    csrf_token = HiddenField()


# Formulaire pour enregistrer son nouveau mot de passe.
class RenamePassword(FlaskForm):
    """
    Formulaire permettant de réinitialiser le mot de passe.

    Attributes :
        new_password (PasswordField) : Nouveau mot de passe.
        confirm_password (PasswordField) : Confirmation du mot de passe.
        csrf_token (HiddenFields) : Jeton CSRF pour la sécurité du formulaire.
    """

    # Champ pour le nouveau password.
    new_password = PasswordField(
        "Nouveau mot de passe utilisateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Nouveau mot de passe."}
    )

    # Champ pour confirmer le password.
    confirm_password = PasswordField(
        "Confirmer le nouveau mot de passe",
        validators=[DataRequired(), EqualTo('new_password', message='Les mots de passe doivent correspondre.')],
        render_kw={"placeholder": "Confirmation du nouveau mot de passe."}
    )

    # Token de sécurité.
    csrf_token = HiddenField()

