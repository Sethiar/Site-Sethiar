"""
Code permettant de se connecter en tant qu'administrateur.
"""
from flask_wtf import FlaskForm

from flask_wtf.file import FileRequired, FileAllowed

from wtforms import StringField, SubmitField, PasswordField, HiddenField, EmailField, FileField, DateField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

from app.Models.user import User


class AdminConnection(FlaskForm):
    """
    Formulaire de connexion pour l'administrateur.

    Attributes :
        pseudo (StringField) : champ pour le pseudo de l'administrateur.
        password (PasswordField) : champ pour le password de l'administrateur.
        submit (SubmitField) : Bouton de soumission du formulaire.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité des formulaires.
    """

    # Champ pour le pseudo.
    pseudo = StringField(
        "Pseudo Administrateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre Pseudo"}
    )

    # Champ pour le rôle.
    role = StringField(
        "Role",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre rôle"}
    )

    # Champ pour le password.
    password = PasswordField(
        "Mot de passe administrateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre mot de passe"}
    )

    # Action de soumettre le formulaire.
    submit = SubmitField("Se connecter au backend")

    # Token de sécurité.
    csrf_token = HiddenField()


class UserAdminSaving(FlaskForm):
    """
        Formulaire d'inscription pour les utilisateurs administrateurs du site.

        Attributes:
            email (EmailField): Champ pour l'adresse e-mail de l'utilisateur.
            pseudo (StringField) : Champ pour le pseudo unique de l'utilisateur.
            role (StringField): Champ pour le rôle de l'utilisateur.
            password (PasswordField) : Champ pour le mot de passe de l'utilisateur.
            password2 (PasswordField) : Champ pour la confirmation du mot de passe de l'utilisateur.
            profil_photo (FileField) : Champ pour télécharger la photo de profil de l'utilisateur.
            date_naissance (DateField) : Champ pour la date de naissance de l'utilisateur.
            submit (SubmitField): Bouton de soumission du formulaire.
            csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.

        Example:
            form = UserAdminSaving()
        """

    # Champ pour l'émail.
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Entrez votre email"}
    )

    # Champ pour le pseudo.
    pseudo = StringField(
        "Pseudo",
        validators=[DataRequired(), Length(min=2, max=30)],
        render_kw={"placeholder": "Votre pseudo"}
    )

    # Champ pour le rôle.
    role = StringField(
        "Rôle",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre rôle"}
    )

    # Champ pour le password.
    password = PasswordField(
        "Mot de passe Utilisateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre mot de passe."})

    # Champ pour la confirmation du password.
    password2 = PasswordField(
        "Confirmer le mot de passe",
        validators=[DataRequired(), EqualTo('password', message='Les mots de passe doivent correspondre.')],
        render_kw={"placeholder": "Confirmation du mot de passe."}
    )

    # Champ pour la date de naissance.
    date_naissance = DateField(
        "Date de naissance",
        validators=[DataRequired()]
    )

    # Champ pour la photo de profil.
    profil_photo = FileField(
        "Photo de profil souhaitée :",
        validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], "Images only !!")]
    )

    # Action de soumettre le formulaire.
    submit = SubmitField(
        "Souscrire aux conditions générales du blog.")

    # Token de sécurité.
    csrf_token = HiddenField()

    # Fonction qui vérifie si le pseudo existe déjà.
    def validate_pseudo(self, pseudo):
        """
        Valide que le pseudo choisi n'existe pas déjà dans la base de données des utilisateurs.

        Args :
            pseudo (StringField): Pseudo à valider.

        Raises :
            ValidationError : Si le pseudo est déjà utilisé.

        """
        user = User.query.filter_by(pseudo=pseudo.data).first()
        if user:
            raise ValidationError('Ce pseudo est déjà utilisé. Veuillez en choisir un autre.')

    # Fonction qui vérifie si l'email existe déjà.
    def validate_email(self, email):
        """
        Valide que l'adresse e-mail n'existe pas déjà dans la base de données des utilisateurs.

        Args :
            email (EmailField): Adresse e-mail à valider.

        Raises :
            ValidationError : Si l'e-mail est déjà utilisé.

        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Cet email est déjà utilisé. Utilisez un autre email.')

    def __repr__(self):
        return f"UserSaving(pseudo='{self.pseudo}', email='{self.email.data}', date de naissance='{self.date_naissance}')"

