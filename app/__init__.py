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

from itsdangerous import URLSafeTimedSerializer

from flask import Flask, request, redirect, url_for, session, g
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_moment import Moment
from flask_mail import Mail
from flask_login import LoginManager
from flask_assets import Environment, Bundle

from app.Models import db
from app.Models.user import User
from app.Models.admin import Admin

# Chargement des variables d'environnement depuis le fichier .env.
load_dotenv()

# Instanciation des extensions Flask.
mailing = Mail()

# Instanciation de Flask-login.
login_manager = LoginManager()


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
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.chat import chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')

    from app.devis import devis_bp
    app.register_blueprint(devis_bp, url_prefix='/devis')

    from app.functional import functional_bp
    app.register_blueprint(functional_bp, url_prefix='/functional')

    from app.frontend import frontend_bp
    app.register_blueprint(frontend_bp, url_prefix='/frontend')

    from app.mail import mail_bp
    app.register_blueprint(mail_bp, url_prefix='/mail')

    from app.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    # Configuration de Flask-Assets
    assets = Environment(app)
    css_bundle = Bundle('SCSS/style.scss', output='gen/style.css', filters='scss')
    assets.register('css_all', css_bundle)

    # Rattachement de Flask-Assets à l'instance Flask.
    app.assets = assets

    # Empêcher le cache durant le développement
    app.config['ASSETS_DEBUG'] = True

    # Forcer la compilation manuelle
    css_bundle.build()

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

    # Configuration du serializer.
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['serializer'] = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')

    # Initialisation de la base de données.
    db.init_app(app)
    # Instanciation de flask-Migrate.
    Migrate(app, db)

    # Pour les réponses JSON concerne l'encodage.
    app.config['JSON_AS_ASCII'] = False

    # Configuration de la protection CSRF.
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Configuration de LoginManager pour utilisateurs.
    login_manager.init_app(app)
    # Redirection automatique vers le formulaire de connexion.
    login_manager.login_view = 'auth.user_connection'

    # Fonction pour charger un utilisateur ou un administrateur.
    @login_manager.user_loader
    def load_user(user_id):
        """
        Charge un utilisateur ou un administrateur en fonction de l'identifiant.

        :param user_id: identifiant de l'utilisateur ou de l'administrateur.

        :return: Instance de User ou de admin.
        """
        # Chargement d'un utilisateur.
        user = User.query.get(int(user_id))
        if user:
            return user

        # Si c'est un admin, chargement d'un admin.
        admin = Admin.query.get(int(user_id))
        if admin:
            return admin

        # Si aucun n'est trouvé, retourne None.
        return None

    # Gestion des utilisateurs non authentifiés.
    @login_manager.unauthorized_handler
    def unauthorized():
        """
        Redirige les utilisateurs non authentifiés vers la page de connexion.

        :return: Redirection vers la page "connexion_requise".
        """
        # Vérification de l'appel de la méthode.
        print("Unathorized handler called")
        return redirect(url_for('auth.user_connection', next=request.url))

    # Injection au sein du contexte global du statut de la connexion.
    @app.context_processor
    def inject_logged_in():
        """
        Injecte le statut de connexion et le pseudo dans le contexte global.

        :return:
        dict: Contexte contenant le statut de la connexion et le pseudo.
        """
        logged_in = session.get("logged_in", False)
        pseudo = session.get("pseudo", None)
        return dict(logged_in=logged_in, pseudo=pseudo)

    # Configuration de la journalisation.
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    handler = logging.FileHandler("fichier.log")
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    return app
