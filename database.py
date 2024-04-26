from factory import create_app, db_client
from flask_sqlalchemy import SQLAlchemy
import datetime


class ClientData(db_client.Model):
    __tablename__ = "client_data"
    id = db_client.Column(db_client.Integer, primary_key=True, nullable=False)
    client_name = db_client.Column(db_client.String(20), nullable=True)
    client_email = db_client.Column(db_client.String(20), unique=True, nullable=True)
    client_phone = db_client.Column(db_client.Integer, unique=True, nullable=True)
    client_legal_service = db_client.Column(db_client.String(30), nullable=True)
    client_case_filed = db_client.Column(db_client.Boolean, nullable=True)
    client_additional_information = db_client.Column(db_client.String(50), nullable=True)
    client_date_booked = db_client.Column(db_client.DateTime, nullable=False, default=datetime.date.today())

    def __repr__(self):
        return (f' ## [ client name={self.client_name} ]'
                f'[ client email={self.client_email} ]'
                f'[ client phone={self.client_phone} ]'
                f'[ client legal service={self.client_legal_service} ]'
                f'[ client case filed?={self.client_case_filed} ]'
                f'[ client additional information={self.client_additional_information} ] ## ')