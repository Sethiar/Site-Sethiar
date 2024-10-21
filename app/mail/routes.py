"""
Code permettant de définir les routes concernant les fonctions de mailing du site de l'entreprise de SethiarWorks.
"""

from app.mail import mail_bp
from flask_mail import Message

from flask import current_app, redirect, url_for, flash


from app.Models.user import User


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

