"""
Code renvoyant le code du formulaire de la demande de devis.
"""

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, TelField, EmailField, SubmitField, SelectField, HiddenField

from wtforms.validators import DataRequired, Email, Length


# Formulaire de demande de devis.
class DevisRequestForm(FlaskForm):
    """
    Formulaire permettant de demander un devis.

    Attributes:
        request_content_devis (TextAreaField): Champ renseignant la nature du projet.
        nom (StringField): Champ renseignant le nom du client.
        prenom (StringField): Champ renseignant le prénom du client.
        telephone (TelField): Champ renseignant le numéro de téléphone.
        email (EmailField): Champ renseignant l'email.
        submit (SubmitField): Bouton pour soumettre le formulaire.
        csrf_token (HiddenField) : Champ caché pour la protection CSRF.

    Example :
        form= DevisRequestForm()
    """

    # Nom et prénom du client.
    nom = StringField(
        "Nom",
        validators=[DataRequired(), Length(max=30)],
        render_kw={"placeholder": "Veuillez renseigner votre nom."}
    )
    prenom = StringField(
        "Prénom",
        validators=[DataRequired(), Length(max=30)],
        render_kw={"placeholder": "Veuillez renseigner votre prénom."}
    )

    # Téléphone du client.
    telephone = TelField(
        "Téléphone",
        validators=[DataRequired()],
        render_kw={"placeholder": "Veuillez renseigner votre numéro de téléphone."}
    )

    # Email du client.
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email(message="Veuillez renseigner votre adresse email.")],
        render_kw={"placeholder": "Veuillez renseigner votre adresse électronique."}
    )

    # Type de projet
    project_type = SelectField(
        "Type de projet",
        choices=[
            ("web", "Développement Web"),
            ("mobile", "Développement Mobile"),
            ("design", "Conception Graphique"),
            ("autre", "Autre")
        ],
        validators=[DataRequired()],
        render_kw={"placeholder": "Choisissez le type de projet"}
    )

    # Le contenu de la demande de devis
    demand_content = TextAreaField(
        "Description du projet",
        validators=[DataRequired(), Length(min=10, message="Veuillez fournir au moins 10 caractères.")],
        render_kw={"placeholder": "Décrivez en quelques mots votre projet (fonctionnalités, objectifs, etc.)."}
    )

    # Bouton de soumission
    submit = SubmitField("Soumettre le devis")

    # Token de sécurité.
    csrf_token = HiddenField()


