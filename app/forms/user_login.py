"""
Code permettant de se connecter en tant qu'utilisateur.
"""

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired


class UserConnection(FlaskForm):
    """
    Formulaire de connexion pour les clients de l'entreprise afin de laisser un commentaire
    .

    Attributes :
        pseudo (StringField) : champ pour le pseudo du client utilisateur.
        password (PasswordField) : champ pour le password de l'utilisateur.
        submit (SubmitField) : Bouton de soumission du commentaire.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité des formulaires.
    """

    # Champ pour le pseudo.
    pseudo = StringField(
        "Pseudo Utilisateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre Pseudo"}
    )

    # Champ pour le password.
    password = PasswordField(
        "Mot de passe utilisateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre mot de passe"}
    )

    # Action de soumettre le formulaire.
    submit = SubmitField("Se connecter")
    csrf_token = HiddenField()


