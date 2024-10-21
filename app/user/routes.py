"""
Code permettant de définir les routes concernant les fonctions des utilisateurs du blog comme l'enregistrement
et l'accès aux formulaires.
"""
import bcrypt

from PIL import Image
from io import BytesIO

from app.Models import db

from app.user import user_bp

from flask import render_template, redirect, url_for, request, flash

from app.forms.user_registration import UserRecording

from app.Models.user import User

from app.extensions import allowed_file


# Route permettant l'affichage du formulaire d'inscription utilisateur.
@user_bp.route("/inscription-client-formulaire", methods=['GET', 'POST'])
def user_registration():
    """
    Route permettant d'afficher le formulaire d'inscription de l'utilisateur
    Gère l'enregistrement d'un nouvel utilisateur. Cette fonction traite à la fois les
    requêtes GET et POST. Lors d'une requête GET, elle affiche le formulaire
    d'enregistrement. Lors d'une requête POST, elle traite les données soumises par
    l'utilisateur, valide le formulaire, gère le fichier de photo de profil, redimensionne
    l'image et enregistre les informations de l'utilisateur dans la base de données.

    :return: Redirection vers la page de confirmation de l'email si l'inscription est réussie,
             sinon redirection vers la page d'enregistrement avec un message d'erreur.
    """
    # Instanciation du formulaire.
    form_usersaving = UserRecording()

    # Vérification de la soumission du formulaire.
    if form_usersaving.validate_on_submit():
        # Assainissement des données.
        pseudo = form_usersaving.pseudo.data
        password_hash = form_usersaving.password.data
        email = form_usersaving.email.data
        date_naissance = form_usersaving.date_naissance.data

        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_hash.encode('utf-8'), salt)

        # Vérification de la soumission du fichier.
        if 'profil_photo' not in request.files or request.files['profil_photo'].filename == '':
            flash("Aucune photo de profil fournie.", "error")
            return redirect(url_for('user.user_registration'))

        profil_photo = request.files['profil_photo']
        if profil_photo and allowed_file(profil_photo.filename):
            photo_data = profil_photo.read()

            # Redimensionnement de l'image avec Pillow.
            try:
                img = Image.open(BytesIO(photo_data))
                img.thumbnail((75,75))
                img_format = img.format if img.format else 'JPEG'
                output = BytesIO()
                img.save(output, format=img_format)
                photo_data_resized = output.getvalue()
            except Exception as e:
                flash(f"Erreur lors du redimensionnement de l'image : {str(e)}", "error")
                return redirect(url_for("user.user_registration"))

            if len(photo_data_resized) > 5 * 1024 * 1024:  # 5Mo
                flash("Le fichier est trop grand (Maximum 5Mo).", "error")
                return redirect(url_for("user.user_registration"))
            photo_data = profil_photo.read()

        else:
            flash("Type de fichier non autoriosé.", "error")
            return redirect(url_for("user.user_registration"))

        new_user = User(
            pseudo=pseudo,
            password_hash=password_hash,
            salt=salt,
            email=email,
            date_naissance=date_naissance,
            # Stockage des données binaires de l'image.
            profil_photo=photo_data_resized
            )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Inscription réussie ! Vous pouvez maintenant vous connecter.')
            return redirect(url_for("mail.send_confirmation_email_user", email=email))
        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de l'enregistrement de l'utilisateur: {str(e)}", "error")

    return render_template('user/user_registration.html', form_usersaving=form_usersaving)

