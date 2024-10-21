"""
Page d'accueil de mon site entreprise
"""
import locale
import os

from flask import render_template, send_from_directory

from app import create_app


# Configurer la localisation en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

app = create_app()


@app.route('/favicon.ico')
def favicon():
    """
    Sert le fichier favicon.ico à partir du répertoire 'static'.
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Route renvoyant l'erreur 404.
@app.errorhandler(404)
def page_not_found(error):
    """
    Renvoie une page d'erreur 404 en cas de page non trouvée.

    Args :
        error : L'erreur qui a déclenché la page non trouvée.

    Returns :
        La page d'erreur 404.
    """
    return render_template("Error/error404.html"), 404


@app.route('/')
def landing_page():
    """

    :return:
    """
    return render_template('Frontend/accueil.html')


# Code lançant l'application.
if __name__ == '__main__':
    app.run(debug=True)

