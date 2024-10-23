"""
Code traiant les fonctionnalités du chat vidéo.
"""
from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, DateField, SubmitField, FileField, TimeField, HiddenField

from flask_wtf.file import FileRequired, FileAllowed

from wtforms.validators import DataRequired


# Formulaire permettant de demander un chat vidéo à l'administrateur.
class ChatRequestForm(FlaskForm):
    """
    Formulaire permettant de demander un chat vidéo à l'administrateur.

    Attributes:
        request_content (TextAreaField): Champ pour le contenu de la demande.
        pseudo (StringField): Champ pour le pseudo de l'utilisateur.
        date_rdv (DateField): Champ pour sélectionner la date du chat vidéo.
        heure (TimeField): Champ pour indiquer l'heure du chat vidéo.
        attachment (FileField): Champ pour joindre un document à la demande de chat.
        submit (SubmitField): Bouton pour soumettre le formulaire.
        csrf_token (HiddenField): Champ caché pour la protection CSRF.

    Example :
        form = ChatRequestForm()
    """

    # Le contenu de la demande.
    request_content = TextAreaField("Contenu de la demande", validators=[DataRequired()],
                                    render_kw={"placeholder": "Veuillez préciser le motif de "
                                                              "votre demande pour le chat vidéo."})

    # Le pseudo de l'utilisateur.
    pseudo = StringField("Pseudo de l'utilisateur", validators=[DataRequired()],
                         render_kw={"placeholder": "Votre pseudo."})

    # La date du chat vidéo.
    date_rdv = DateField("Veuillez sélectionner la date souhaitée", validators=[DataRequired()],
                         render_kw={"placeholder": "Date souhaitée pour le chat vidéo :"})

    # L'heure souhaitée.
    heure = TimeField("Heure souhaitée", format='%H:%M', validators=[DataRequired()],
                      render_kw={"placeholder": "12:00"})

    attachment = FileField("Joindre un document", validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc', 'docx'], 'Seuls les fichiers PDF ou Word sont autorisés.')
    ])
    # Action de soumettre le formulaire.
    submit = SubmitField("Soumettre la demande")

    csrf_token = HiddenField()


# Formulaire permettant d'envoyer le lien pour la session de chat vidéo.
class UserLink(FlaskForm):
    """
    Formulaire pour envoyer le lien à l'utilisateur.
    """
    chat_link = StringField('Chat_link', validators=[DataRequired()],
                            render_kw={"placeholder": "Veuillez renseigner le lien copié."})
    csrf_token = HiddenField()
    submit = SubmitField('Envoyer')