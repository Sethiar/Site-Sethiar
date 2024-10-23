"""
Code permettant à l'utilisateur de s'inscrire dans la base de données.
"""
from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField, FileField, DateField, SubmitField, HiddenField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.Models.user import User


# Classe permettant d'enregistrer les utilisateurs dans la table de données User.
class UserRecording(FlaskForm):
    """
    Formulaire d'inscription pour les utilisateurs du site.

    Attributes:
        pseudo (StringField) : Champ pour le pseudo utilisateur.
        email (EmailField) : Champ pour l'email de l'utilisateur.
        password (PasswordField) : Champ pour le password e l'utilisateur.
        password2 (PasswordField) : Champ pour la vérification du password.
        profil_photo (FileField) : Champ pour la sauvegarde de la photo de profil utilisateur.
        date_naissance (DateField) : Champ pour la date de naissance.
        submit (SubmitField) : Bouton de soumission du formulaire.
        csrf_token (HiddenField) : Jeton CSRF.

        Exemple :
            form = UserRecording()
    """
    pseudo = StringField(
        "Pseudo", validators=[DataRequired(), Length(min=2, max=30)],
        render_kw={"placeholder": "Entrez votre pseudo"}
    )
    email = EmailField(
        "Email", validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Entrez votre Email"}
    )
    password = PasswordField(
        "Password", validators=[DataRequired()],
        render_kw={"placeholder": "Mot de passe utilisateur"}
    )
    password2 = PasswordField(
        "Confirmer password",
        validators=[DataRequired(), EqualTo('password', message="Les mots de passe doivent correspondre")],
        render_kw={"placeholder": "Confirmation du mot de passe."}
    )
    date_naissance = DateField(
        "Date de naissance",
        validators=[DataRequired()]
    )
    profil_photo = FileField("Photo de profil souhaitée :",
                             validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], "Images seulement !!")]
                             )
    csrf_token = HiddenField()
    submit = SubmitField(
        "Souscrire aux conditions générales du site."
    )

    # Fonction vérifiant la bonne créations du formulaire.

    # Fonction qui vérifie si le pseudo existe déjà.
    def validate_pseudo(self, pseudo):
        """
        Valide le pseudo choisi si il n'existe pas déjà dans la table de données User.

        Args :
            pseudo (StringField): Pseudo à vérifier.

        Raise :
            ValidationError : Si le pseudo est déjà utilisé.
        """
        user = User.query.filter_by(pseudo=pseudo.data).first()
        if user:
            raise ValidationError('Ce pseudo est déjà utilisé. Veuillez en choisir un autre.')

    def validate_email(self, email):
        """
        Valide l'email choisi s'il n'existe pas déjà dans la table de données User.

        Args :
            email (EmailField): EMail à vérifier.

        Raise :
            ValidationError : Si l'email est déjà utilisé.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Cet email est déjà utilisé. Veuillez en choisir une autre.')

    def __repr__(self):
        return f"UserRecording(pseudo='{self.pseudo}', email='{self.email.data}'," \
               f" date de naissance='{self.date_naissance}'"

