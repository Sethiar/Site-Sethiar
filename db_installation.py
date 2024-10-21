"""
Fichier permettant d'installer les tables de données de la base PostGreSQL.
"""
from flask_login import UserMixin
from app.Models import db

from datetime import datetime

# Utilisation de JSON pour PostgreSQL.
from sqlalchemy.dialects.postgresql import JSON

from app import create_app

app = create_app()

# L'installation des tables de données dans un contexte d'application.
with app.app_context():

    class Admin(db.Model, UserMixin):
        """
        Modèle de données représentant un administrateur.

        Attributes :
            id (int): identifiant de l'administrateur.
            pseudo (str): Pseudo de l'administrateur.
            role (str): rôle de l'administrateur.
            password_hash (LB): Mot de passe hashé.
            salt (LB): Salage du mot de passe.
        """

        __tablename__ = "admin"
        __table_args__ = {"extend_existing": True}

        id = db.Column(db.Integer, primary_key=True)
        pseudo = db.Column(db.String(20), nullable=False)
        role = db.Column(db.String(20), nullable=False)
        email = db.Column(db.String(20), nullable=False)
        profil_photo = db.Column(db.LargeBinary, nullable=True)
        password_hash = db.Column(db.LargeBinary(255), nullable=False)
        salt = db.Column(db.LargeBinary(255), nullable=False)

        # Relation avec la table ChatRequest.
        chat_requests = db.relationship('ChatRequest', back_populates='admin', cascade='all, delete-orphan')

    class ChatRequest(db.Model):
        """
        Modèle de données représentant une demande de chat vidéo.

        Attributes :
            id (int): Identifiant unique de la demande.
            pseudo (str): Pseudo de l'utilisateur.
            request_content (str): Contenu de la requête.
            date_rdv (datetime): Date initiale proposée par l'utilisateur.
            heure (time): Heure proposée par l'utilisateur.
            status (StatusEnum): Statut de la demande (en attente, approuvé, rejeté).
            admin_choices (list): Stocke les choix de créneaux proposés par l'administrateur.
            user_choice (datetime): Stocke le choix final de l'utilisateur.
            created_at (datetime): Date et heure de création de la demande.
        """

        __tablename__ = "chat_request"
        __table_args__ = {"extend_existing": True}

        id = db.Column(db.Integer, primary_key=True)
        pseudo = db.Column(db.String(30), nullable=False)
        request_content = db.Column(db.Text, nullable=False)
        date_rdv = db.Column(db.DateTime(timezone=True), nullable=False)
        heure = db.Column(db.Time(), nullable=False)
        attachment = db.Column(db.String(255), nullable=True)
        status = db.Column(db.String(20), nullable=False, default='en attente')
        admin_choices = db.Column(JSON, nullable=True)  # Stocke les créneaux comme liste de strings ou datetimes
        user_choice = db.Column(db.DateTime(timezone=True), nullable=True)
        created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)

        # Relation avec la classe User.
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        user = db.relationship('User', back_populates='chat_requests')

        # Relation avec la classe Admin.
        admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
        admin = db.relationship('Admin', back_populates='chat_requests')

    class User(db.Model, UserMixin):
        """
        Modèle de données représentant un utilisateur de l'application.

        Attributes:
            id (int) : Identifiant unique de l'utilisateur.
            pseudo (str) : Pseudo unique de l'utilisateur.
            password_hash (bytes) : Mot de passe hashé de l'utilisateur.
            salt (bytes) : Salage du mot de passe.
            email (str) : Adresse e-mail de l'utilisateur.
            date_naissance (datetime.date) : Date de naissance de l'utilisateur.
            profil_photo (bytes) : Photo de profil de l'utilisateur en format binaire.
            role (str) : Par défault c'est utilisateur si enregistrement via le Frontend.
            banned (bool) : Indique si l'utilisateur est banni (par défaut False).
            date_banned : Indique la date de début du bannissement.
            date_ban_end : Permet de définir la date de fin du bannissement.
            count_ban : Visualise le nombre de ban de l'utilisateur.
        """

        __tablename__ = "user"
        __table_args__ = {"extend_existing": True}

        id = db.Column(db.Integer, primary_key=True)
        pseudo = db.Column(db.String(30), nullable=False, unique=True)
        role = db.Column(db.String(30), default='Utilisateur')
        password_hash = db.Column(db.LargeBinary(255), nullable=False)
        salt = db.Column(db.LargeBinary(254), nullable=False)
        email = db.Column(db.String(255), nullable=False)
        date_naissance = db.Column(db.Date, nullable=False)
        profil_photo = db.Column(db.LargeBinary, nullable=False)
        chemin_photo = db.Column(db.String(255), nullable=True)
        banned = db.Column(db.Boolean, default=False)
        date_banned = db.Column(db.DateTime, nullable=True)
        date_ban_end = db.Column(db.DateTime, nullable=True)
        count_ban = db.Column(db.Integer, default=0)

        # Relation entre la demande de chat et la classe user.
        chat_requests = db.relationship('ChatRequest', back_populates='user', cascade='all, delete-orphan')


    # Création de toutes les tables à partir de leur classe.
    db.create_all()

print("Félicitations, toutes vos tables ont été installées.")