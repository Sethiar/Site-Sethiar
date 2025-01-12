"""
Code fournissant les formulaires permettant à un utilisateur de poster
dans la section du forum du site entreprise SethiarWorks.
"""

from flask_wtf import FlaskForm

from wtforms import HiddenField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# Formulaire permettant à un utilisateur de poster un commentaire en réponse à un sujet du forum.
class CommentSubjectForm(FlaskForm):
    """
    Formulaire pour ajouter un commentaire à un sujet de la section forum du site entreprise SethiarWorks.

    Attributes :
        comment_content (TextAreaField) : contenu du commentaire.
        user_pseudo (StringField) : Champ pour le pseudo de l'utilisateur.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.

    Example :
        form = CommentSubjectForm()
    """

    # Contenu du commentaire.
    comment_content = TextAreaField(
        "Contenu du commentaire",
        validators=[DataRequired()],
        render_kw={"placeholder": "Saisie du commentaire"}
    )

    # Pseudo de l'utilisateur.
    user_pseudo = StringField(
        "Pseudo de l'utilisateur",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre pseudo"}
    )

    # Action de soumettre le formulaire.
    submit = SubmitField("Soumettre le commentaire")
    csrf_token = HiddenField()


# Formulaire permettant à l'utilisateur de modifier son commentaire pour la section
# forum du site de l'entreprise SethiarWorks.
class ChangeCommentSubjectForm(FlaskForm):
    """
    Formulaire permettant de modifier un commentaire par l'utilisateur.

    Attributes :
        comment_content (TextAreaField) : Contenu du commentaire de l'utilisateur.
        submit (SubmitField) : Bouton de soumission du formulaire.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.
    """

    # Contenu du commentaire.
    comment_content = TextAreaField(
        "Contenu du commentaire",
        validators=[DataRequired()],
        render_kw={"placeholder": "Saisie du commentaire"}
    )

    # Action de soumettre le commentaire.
    submit = SubmitField("Soumettre le commentaire")
    csrf_token = HiddenField()


# Formulaire permettant à un utilisateur de supprimer son commentaire.
class SuppressCommentForm(FlaskForm):
    """
    Formulaire permettant à l'utilisateur de supprimer son commentaire.

    Attributes :
        submit (SubmitField) : Bouton de soumission du formulaire.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.
    """
    # Action de soumettre le commentaire.
    submit = SubmitField("Supprimer le commentaire")
    csrf_token = HiddenField()


# Formulaire permettant de supprimer les commentaires dans la section forum au niveau du backend.
class SuppressCommentSubjectForm(FlaskForm):
    """
    Formulaire pour supprimer un commentaire de la section forum au niveau du backend.

    Attributes :
        comment_id (HiddenField) : Champ caché pour l'ID du commentaire à supprimer.
        submit (SubmitField): Bouton de soumission du formulaire.
    """

    # ID du commentaire à supprimer.
    comment_id = HiddenField(
        "Comment_id",
        validators=[DataRequired()]
    )

    # Action de soumettre le commentaire.
    submit = SubmitField('Supprimer')


# Formulaire permettant de répondre à un commentaire dans la section forum.
class ReplySubjectForm(FlaskForm):
    """
    Formulaire permettant d'ajouter une réponse à un commentaire dans la section forum.

    Attributes :
        reply_content (TextAreaField) : Champ de texte pour la réponse au commentaire.
        comment_id (HiddenField) : Champ caché pour l'ID du commentaire parent.
        submit (SubmitField) : Bouton de soumission du commentaire.
        csrf_token (HiddenField) : Jeton pour la sécurité du formulaire.
    """

    # Contenu de la réponse.
    reply_content = TextAreaField(
        "Réponse au commentaire",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre réponse"}
    )

    # Champ pour stocker l'ID du commentaire parent.
    comment_id = HiddenField("ID du commentaire")

    # Action de soumettre le commentaire.
    submit = SubmitField("Soumettre la réponse")
    csrf_token = HiddenField()


# Formulaire permettant à un utilisateur de modifier sa réponse à un commentaire.
class ChangeReplySubject(FlaskForm):
    """
    Formulaire permettant à un utilisateur de modifier sa réponse.

    Attributes :
        reply_content : Contenu du commentaire de l'utilisateur.
        submit (SubmitField) : Bouton de soumission du commentaire.
        csrf_token (HiddenField) : Jeton CSRF pour la sécurité du formulaire.
    """

    # Contenu de la réponse.
    reply_content = TextAreaField(
        "Contenu de la réponse",
        validators=[DataRequired()],
        render_kw={"placeholder": "Votre réponse"}
    )

    # Action de soumettre le commentaire.
    submit = SubmitField("Soumettre la réponse")
    csrf_token = HiddenField()


# Formulaire permettant à un utilisateur de supprimer sa réponse à un commentaire.
class SuppressReplySubject(FlaskForm):
    """
    Formulaire permettant à un utilisateur de supprimer sa réponse à un commentaire.

    Attributes :
        reply_id (HiddenField) : Champ caché pour l'ID de la réponse à supprimer.
        submit (SubmitField): Bouton de soumission du formulaire.
    """

    reply_id = HiddenField(
        "reply_id",
        validators=[DataRequired()]
    )

    # Action de soumettre le commentaire.
    submit = SubmitField('Supprimer')


# Formulaire permettant de liker un commentaire dans la section forum.
class CommentLike(FlaskForm):
    """
    Formulaire permettant de liker un commentaire.

    Attributes :
        csrf_token (HiddenField) : Jeton csrf_token pour la sécurité des commentaires.
        submit (SubmitField): Bouton de soumission du formulaire.

    Example:
        form = CommentLike()
    """

    csrf_token = HiddenField()

    # Action de soumettre le commentaire.
    submit = SubmitField()
