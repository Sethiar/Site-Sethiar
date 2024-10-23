"""
Code permettant de définir les routes concernant les fonctions des utilisateurs du site du frontend.
"""

from flask import render_template, abort


from flask_login import current_user

from app.frontend import frontend_bp

from app.forms.subject_forum import NewSubjectForumForm
from app.Models.subject_forum import SubjectForum
from app.Models.comment_subject import CommentSubject
from app.Models.likes_comment_subject import CommentLikeSubject
from app.Models.reply_subject import ReplySubject


from app.forms.form_comment import CommentSubjectForm, CommentLike, SuppressCommentForm, SuppressReplySubject


# Route permettant d'accéder au forum su site entreprise SethiarWoks.
@frontend_bp.route('accès-forum')
def forum():
    """
    Route permettant d'accéder à la page du forum du site.

    :return: templates HTML 'frontend/forum.html.
    """
    # Instanciation du formulaire.
    formsubjectforum = NewSubjectForumForm()

    # Récupération de tous les sujets de la table de données.
    subjects = SubjectForum.query.all()

    # Passage de la valuer booléenne d'authentification.
    is_authenticated = current_user.is_authenticated

    # Debug : Vérification du type.
    print("Type of is_authenticated : ", type(is_authenticated))

    return render_template('frontend/forum.html', formsubjectforum=formsubjectforum, subjects=subjects,
                           is_authenticated=is_authenticated)


# Route afin de visualiser un sujet du forum particulier.
@frontend_bp.route("/accès-sujet-forum/<int:subject_id>", methods=['GET', 'POST'])
def forum_subject(subject_id):
    """
    Route permettant d'accéder à un sujet spécifique du forum.

    Args:
        subject_id (int) : L'identifiant du sujet à afficher.

    Returns :
        Template HTML 'frontend/subject_forum.html' avec les détails du sujet et ses commentaires associés.

    Raises :
        404 Error : Si aucun sujet correspondant à l'ID spécifié n'est trouvé dans la base de données.
    """
    # Création de l'instance des formulaires.
    formcomment = CommentSubjectForm()
    formlikecomment = CommentLike()
    formsuppress = SuppressCommentForm()
    formsuppressreply = SuppressReplySubject()

    # Récupération du sujet spécifié par l'ID depuis la base de données.
    subject = SubjectForum.query.get_or_404(subject_id)

    # Passage de la valeur booléenne d'authentification au template.
    is_authenticated = current_user.is_authenticated

    # Debug : Vérification du type.
    print("Type of is authenticated : ", type(is_authenticated))

    # Vérification de l'existence du sujet.
    if not subject:
        # Si le sujet n'existe pas dans la base de données, erreur 404 renvoyée.
        abort(404)

    # Récupération des commentaires associés à ce sujet.
    comment_subject = CommentSubject.query.filter_by(subject_id=subject_id)

    # Préparation des données de likes pour chaque commentaire.
    comment_likes_data = {}
    for comment in comment_subject:
        like_count = CommentLikeSubject.query.filter_by(comment_id=comment.id).count()
        liked_user_ids = [like.user_id for like in CommentLikeSubject.query.filter_by(comment_id=comment.id).all()]
        liked_by_current_user = current_user.is_authenticated and current_user.id in liked_user_ids
        comment_likes_data[comment.id] = {
            "like_count": like_count,
            "liked_user_ids": liked_user_ids,
            "liked_by_current_user": liked_by_current_user
        }
    return render_template("Frontend/subject_forum.html", subject=subject, subject_id=subject_id,
                               formsuppress=formsuppress, formsuppressreply=formsuppressreply,
                               comment_subject=comment_subject, formcomment=formcomment,
                               formlikecomment=formlikecomment, comment_likes_data=comment_likes_data,
                               is_authenticated=is_authenticated)
