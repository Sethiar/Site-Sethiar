"""
Code permettant de définir les routes concernant les fonctions de mailing du site de l'entreprise de SethiarWorks.
"""

from app.mail import mail_bp
from flask_mail import Message

from flask import current_app, redirect, url_for, flash

from app.Models.user import User

from app.email_utils import send_email_in_background


@mail_bp.route('envoi-pour-confirmer-inscription/<string:email>')
def send_confirmation_email_user(email):
    """
    Fonction qui envoie un mail automatique de confirmation d'inscription au site de l'entreprise SethiarWorks.

    :param email: Email de l'utilisateur nouvellement inscrit.
    :return:
    """
    user = User.query.filter_by(email=email).first()
    if not user:
        flash("Utilisateur non trouvé.", "Attention")
        return redirect(url_for('landing_page'))

    # Corps du message.
    msg = Message("Confirmation d'inscription", sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[email])
    msg.body = f"Bonjour {user.pseudo} \n" \
               "\n" \
               f"Merci de vous être inscrit sur le site de l'entreprise SethiarWorks. " \
               f"Votre inscription a été confirmée avec succès.\n" \
               "\n" \
               f"Nous espérons que nous vous retrouverons bientôt afin de créer votre besoin selon nos soins.\n" \
               f"Merci {user.pseudo} de votre confiance. \n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."

    current_app.extensions['mail'].send(msg)
    return redirect(url_for('landing_page'))


# Méthode qui avertit l'utilisateur de son bannissement pendant 7 jours.
def mail_banned_user(email):
    """
    Envoie un e-mail informant un utilisateur de son bannissement temporaire pour non-respect des règles.

    :param email: email de l'utilisateur qui subit le bannissement.
    :return : retour sur la page admin.
    """
    user = User.query.filter_by(email=email).first()

    msg = Message("Bannissement",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               "\n" \
               f"Suite à la tenue des règles en vigueur sur le site de l'entreprise SethiarWorks, vous avez été banni " \
               f"pendant une semaine. J'espère que vous comprenez notre démarche. Si vous ne respectez pas " \
               f"à nouveau les règles du site, vous serez banni définitivement.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui envoie un mail prévenant de la fin du bannissement.
def mail_deban_user(email):
    """
    Envoie un e-mail informant un utilisateur de la fin de son bannissement.

    :param email: email de l'utilisateur qui subit le bannissement.
    :return: retour sur la page admin.
    """
    user = User.query.filter_by(email=email).first()
    msg = Message("Fin de bannissement",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email])
    msg.body = f"Bonjour {user.pseudo}, \n" \
               "\n" \
               f"Nous vous informons que vous n'êtes plus banni du site de l'entreprise SethiarWorks. \n" \
               f"Nous espérons vous revoir très vite. \n" \
               f"À bientôt.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."

    current_app.extensions['mail'].send(msg)


# Méthode qui permet d'avertir l'utilisateur de son bannissement définitif du blog.
def definitive_banned(email):
    """
    Envoie un e-mail informant un utilisateur de son bannissement définitif du blog pour récidive
    dans le non-respect des règles.

    :param email: email de l'utilisateur qui subit le bannissement.
    """
    user = User.query.filter_by(email=email).first()
    msg = Message("Effacement des bases de données.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               "\n" \
               f"Comme nous vous l'avions indiqué dans un précédent mail, si vous étiez de nouveau sujet à un rappel " \
               f"à l'ordre sur le respect des règles en vigueur sur notre site, vous seriez définitivement bloqué de " \
               f"nos bases de données. Le fait que vous receviez ce mail signifie que vous avez été banni. \n" \
               "\n" \
               f"Nous regrettons cette décision, mais nous ne pouvons tolérer ce manquement aux " \
               f"règles établies.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui envoie le lien permettant de faire le changement du mot de passe.
def reset_password_mail(email, reset_url):
    """
    Envoie un mail afin de cliquer sur un lien permettant la réinitialisation du mot de passe.
    Si l'utilisateur n'est pas à l'origine de cette action, le mail inclut un lien d'alerte pour l'administrateur.

    :param reset_url: URL pour réinitialiser le mot de passe
    :param email: Adresse email du destinataire
    :return: None
    """
    user = User.query.filter_by(email=email).first()
    if not user:
        flash("Utilisateur non trouvé.", "attention")
        return redirect(url_for('landing_page'))
    msg = Message('Réinitialisation de votre mot de passe',
                  sender='noreply@yourapp.com',
                  recipients=[email])
    msg.body = f'Bonjour {user.pseudo},\n' \
               "\n" \
               f' pour réinitialiser votre mot de passe, cliquez sur le lien suivant : {reset_url}' \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui envoie un mail assurant le succès de la réinitialisation du mail.
def password_reset_success_email(user):
    """
    Envoie un e-mail de confirmation de réinitialisation de mot de passe à l'utilisateur.

    :param user: Instance de l'utilisateur.
    """
    msg = Message('Confirmation de réinitialisation de mot de passe',
                  sender='noreply@yourapp.com',
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               "\n" \
               f"Votre mot de passe a été réinitialisé avec succès.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui permet d'envoyer un mail à un utilisateur si quelqu'un a
# répondu à son commentaire dans la section forum.
def mail_reply_forum_comment(email, subject_nom):
    """
    Envoie un mail à l'auteur du commentaire en cas de réponse à celui-ci.
    :param email: email de l'utilisateur qui a commenté le sujet du forum.
    :param subject_nom : nom du sujet du forum commenté.
    """
    user = User.query.filter_by(email=email).first()

    msg = Message("Quelqu'un a répondu à votre commentaire de la section forum.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               "\n" \
               f"Un utilisateur a répondu à votre commentaire de la section forum dont le sujet est {subject_nom}.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui envoie un mail à utilisateur en cas de like de son commentaire à la section forum.
def mail_like_comment_subject(user, subject):
    """
    Envoie un mail à l'auteur du commentaire de la section forum afin de l'avertir
    qu'un utilisateur a aimé son commentaire.
    :param user: utilisateur qui a posté le commentaire.
    :param subject: sujet dont le commentaire a été liké.
    """
    msg = Message("Quelqu'un a aimé votre commentaire de la section forum.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               "\n" \
               f"Un utilisateur a aimé votre commentaire de la section forum " \
               f"concernant le sujet suivant : {subject.nom}.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    send_email_in_background(current_app._get_current_object(), msg)


# Méthode qui permet d'envoyer un mail à un utilisateur si quelqu'un a
# répondu à son commentaire dans la section vidéo.
def mail_reply_video_comment(email, video_title):
    """
    Envoie un mail à l'auteur du commentaire en cas de réponse à celui-ci.
    :param email: email de l'utilisateur qui a commenté le sujet du forum.
    :param video_title : titre de la vidéo commentée.
    """
    user = User.query.filter_by(email=email).first()

    msg = Message("Quelqu'un a répondu à votre commentaire de la section vidéo.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               "\n" \
               f"Un utilisateur a répondu à votre commentaire de la section vidéo dont le titre est {video_title}.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui envoie un mail à utilisateur en cas de like de son commentaire à la section vidéo.
def mail_like_comment_video(user, video):
    """
    Envoie un mail à l'auteur du commentaire de la section vidéo afin de l'avertir
    qu'un utilisateur a aimé son commentaire.
    :param user: utilisateur qui a posté le commentaire.
    :param video: vidéo dont le commentaire a été liké.
    """
    msg = Message("Quelqu'un a aimé votre commentaire de la section vidéo.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo},\n" \
               f"Un utilisateur a aimé votre commentaire de la section vidéo " \
               f"concernant le sujet suivant : {video.title}.\n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    send_email_in_background(current_app._get_current_object(), msg)


# Méthode envoyant un mail de confirmation de la demande de chat vidéo à l'utilisateur.
def send_confirmation_request_reception(user):
    """
    Fonction qui envoie un mail de confirmation à l'utilisateur de la bonne réception de sa requête de chat vidéo.

    :param user: utilisateur qui a fait la requête de chat vidéo.
    :return:
    """
    msg = Message("Confirmation de la demande de chat vidéo.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo} \n" \
               f"nous vous confirmons la bonne réception de votre demande \n" \
               f"et nous vous répondrons dans les plus brefs délais " \
               f"afin de valider votre rendez-vous. \n" \
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode envoyant un mail à l'administrateur du site s'il y a une demande de chat vidéo.
def send_request_admin(user, request_content, attachment_data=None, attachment_name=None):
    """
    Fonction qui envoie un mail pour informer l'administration d'une requête de chat vidéo.

    :param user: utilisateur qui a envoyé la demande de chat.
    :param request_content: contenu de la requête de l'utilisateur.
    :attachment_data (bytes): Le contenu du fichier à envoyer (en mémoire).
    attachment_name (str): Le nom du fichier à envoyer.
    """
    msg = Message("Demande de chat vidéo.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[current_app.config['MAIL_DEFAULT_SENDER']])
    msg.body = f"Bonjour Sethiar, \n" \
               "\n" \
               f"{user.pseudo} souhaite avoir un chat vidéo avec vous.\n" \
               f"Voici sa requête :\n" \
               f"{request_content} \n" \
               "\n" \
               f"Bon courage Mec."

    # Si un fichier est joint, ajout en pièce jointe depuis la mémoire.
    if attachment_data and attachment_name:
        msg.attach(attachment_name, "application/octet-stream", attachment_data)

    current_app.extensions['mail'].send(msg)


# Fonction envoyant un mail à l'utilisateur en générant le lien de connexion au chat vidéo.
def send_mail_validate_request(user, request, chat_link):
    """
    Fonction qui envoie un mail pour informer de la validation de la requête par l'administrateur.
    :param user: utilisateur qui a envoyé la demande de chat.
    :param request: requête de l'utilisateur.
    :param chat_link: lien du chat vidéo.
    :return:
    """

    msg = Message("Validation de la requête de chat vidéo.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo}, \n" \
               "\n" \
               f"Titi a accepté votre requête de chat vidéo.\n" \
               f"Le rendez-vous est prévu le {request.date_rdv} à {request.heure}.\n" \
               f"Voici le lien de connexion: {chat_link}\n" \
               f"Nous vous demandons de cliquer sur ce lien quelques minutes " \
               f"avant le rendez-vous afin d'être prêt pour le chat vidéo.\n" \
               "\n"\
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)


# Méthode qui envoie un mail de refus de la requête de chat vidéo.
def send_mail_refusal_request(user):
    """
    Fonction qui envoie un mail pour informer du refus de la requête par l'administrateur.

    :param user: utilisateur qui a envoyé la demande de chat.
    :return:
    """
    msg = Message("Refus de la requête de chat vidéo.",
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f"Bonjour {user.pseudo}, \n" \
               "\n" \
               f"Titi est dans l'impossibilité de valider votre rendez-vous. \n" \
               f"Afin de renouveler votre demande, nous vous prions de bien vouloir "\
               f"refaire une demande de chat vidéo. \n"\
               "\n" \
               f"Cordialement, \n" \
               f"L'équipe du site de SethiarWorks."
    current_app.extensions['mail'].send(msg)

