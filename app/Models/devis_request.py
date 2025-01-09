"""
Code permettant de créer la classe devis_request.
"""

from app import db

from datetime import datetime


class DevisRequest(db.Model):
    """
    Modèle de données représentant une demande de devis.

    Attributes :
        id (int) : Identifiant unique de la demande de devis.
        nom (str) : Nom du client.
        prenom (str) : Prénom du client.
        telephone (str) : Téléphone du client.
        email (str) : Email du client.
        project_type (str): Type de projet demandé.
        request_content (str) : Description de la demande de devis.
        date_devis (datetime) : Date de la demande de devis.
        status (StatusEnum) : Statut de la demande (en attente, approuvé, rejeté).
        created_at (datetime) : Date et heure de la validation de la demande de devis.
    """

    __tablename__ = "devis_request"
    ___table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    project_type = db.Column(db.String(20), nullable=False)
    demand_content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="en attente")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """
        Représentation en chaîne de caractères de l'objet DevisRequest

        Returns :
            str : Chaîne de caractère représentant l'objet DevisRequest.
        """
        return (f"<DevisRequest(id={self.id}, nom={self.nom}, prenom={self.prenom}, "
                f"telephone={self.telephone}, email={self.email}, project_type={self.project_type}, "
                f"demand_content={self.demand_content}, status={self.status}, created_at={self.created_at})>")

    # Fonction qui permet de valider la demande de devis et ainsi de modifier le statut de la demande.
    def waiting_request_validate(self, new_status):
        """
        Validation de la demande de chat vidéo. Par défaut, le statut est 'en attente'.

        Parameters:
            new_status (str): Le nouveau statut de la demande ('validée', 'refusée').
        """
        if new_status not in ['validée', 'refusée']:
            raise ValueError("Le statut doit être 'en attente', 'validée' ou 'refusée'.")

        self.status = new_status
        try:
            db.session.commit()
        except Exception as e:
            # Retour en arrière en cas d'erreur
            db.session.rollback()
            raise e
        finally:
            # Fermer la session proprement
            db.session.close()

    # Fonction qui permet de refuser la demande de devis et ainsi de modifier le statut de la demande.
    def waiting_request_refusal(self, new_status):
        """
        Refus de la demande de chat vidéo. Par défaut, le statut est 'en attente'.

        Parameters:
            new_status (str): Le nouveau statut de la demande ('validée', 'refusée').
        """
        if new_status not in ['validée', 'refusée']:
            raise ValueError("Le statut doit être 'en attente', 'validée' ou 'refusée'.")

        self.status = new_status
        try:
            db.session.commit()
        except Exception as e:
            # Retour en arrière en cas d'erreur
            db.session.rollback()
            raise e
        finally:
            # Fermer la session proprement
            db.session.close()

