"""
Fichier de configuration de mon site entreprise SethiarWorks
"""

import os
import logging
import secrets
import config.config

from datetime import timedelta
from config.config import Config

from dotenv import load_dotenv

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_moment import Moment
from flask_mail import Mail


from app.Models import db

# Chargement des variables d'environnement depuis le fichier .env.
load_dotenv()

# Instanciation des extensions Flask.
mailing = Mail()


# Création de l'instance pour le site de l'entreprise.
def create_app():
    """
    Crée et configure l'application Flask pour le site SethiarWorks.

    Returns:
        Flask app: Instance de l'application Flask configurée.
    """

    # Création de l'application Flask.
    app = Flask("SethiarWorks")

    # Configuration de flask-moment.
    moment = Moment(app)

    # Création des blueprints pour ordonner les routes.
    from app.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/Admin')

    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.chat import chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')

    from app.functional import functional_bp
    app.register_blueprint(functional_bp, url_prefix='/functional')

    from app.frontend import frontend_bp
    app.register_blueprint(frontend_bp, url_prefix='/frontend')

    from app.mail import mail_bp
    app.register_blueprint(mail_bp, url_prefix='/mail')

    from app.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    # Configuration du mailing Flask.
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
    app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    mailing.init_app(app)

    # Propagation des erreurs aux gestionnaires d'erreurs des Blueprints.
    app.config['PROPAGATE_EXCEPTIONS'] = True

    # Chargement de la configuration de l'environnement.
    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_object(config.config.DevelopmentConfig)
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object(config.config.TestingConfig)
    else:
        app.config.from_object(config.config.ProductConfig)

    # Configuration de l'environnement de l'application.
    app.config.from_object(Config)

    app.config["SESSION_COOKIE_SECURE"] = True

    # Configuration de la durée de vie des cookies de session.
    app.permanent_session_lifetime = timedelta(days=1)

    # Définition de la clé secrète pour les cookies.
    app.secret_key = secrets.token_hex(16)

    # Initialisation de la base de données.
    db.init_app(app)
    # Instanciation de flask-Migrate.
    Migrate(app, db)

    # Pour les réponses JSON concerne l'encodage.
    app.config['JSON_AS_ASCII'] = False

    # Configuration de la protection CSRF.
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Configuration de la journalisation.
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    handler = logging.FileHandler("fichier.log")
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    return app
