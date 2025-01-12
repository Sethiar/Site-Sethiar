"""
Code fournissant les formulaires concernant les sujets du forum du site de l'entreprise SethiarWorks.
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, HiddenField
from wtforms.validators import DataRequired


# Formulaire permettant la création d'un nouveau sujet sur le forum.
class NewSubjectForumForm(FlaskForm):
    """
    Formulaire pour ajouter un nouveau sujet sur le forum.

    Attributes:
        nom (StringField) : Champ pour le nom du sujet pour le forum.

    Example :
        form = NewSubjectForumForm()
    """
    # Nom du sujet.
    nom = StringField(
        "Sujet",
        validators=[DataRequired()],
        render_kw={'placeholder': "Nouveau sujet"}
    )

    # Action de soumettre le formulaire.
    submit = SubmitField("Ajouter le sujet")
    csrf_token = HiddenField()


# Formulaire permettant de supprimer un sujet du forum.
class SuppressSubject(FlaskForm):
    """
    Formulaire pour supprimer un sujet de la section forum.

    Attributes :
        subject_id (HiddenField) : Champ caché pour l'ID du sujet à supprimer.
        submit (SubmitField): Bouton de soumission du formulaire.
    """
    # Champ caché pour l'id du sujet.
    subject_id = HiddenField(
        'Subject_id',
        validators=[DataRequired()]
    )

    # Action de soumettre le formulaire.
    submit = SubmitField('Supprimer')

    # Token de sécurité.
    csrf_token = HiddenField()

