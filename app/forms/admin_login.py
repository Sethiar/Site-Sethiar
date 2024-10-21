"""
Code permettant de se connecter en tant qu'administrateur.
"""

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired


class AdminConnection(FlaskForm):
    """
    Formulaire de connexion pour l'administrateur.

    Attributes :
        pseudo (StringField) : champ pour le pseudo de l'administrateur.
        password (PasswordField) : champ pour le password de l'administrateur.
        submit (SubmitField) : Bouton de soumission du formulaire.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité des formulaires.
    """
    pseudo = StringField("Pseudo Administrateur", validators=[DataRequired()],
                         render_kw={"placeholder": "Votre Pseudo"})
    role = StringField('Role', validators=[DataRequired()],
                       render_kw={"placeholder": "Votre rôle"})
    password = PasswordField("Mot de passe administrateur", validators=[DataRequired()],
                             render_kw={"placeholder": "Votre mot de passe"})
    submit = SubmitField("Se connecter au backend")
    csrf_token = HiddenField()
