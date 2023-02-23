from db import db
# from datetime import datetime
# from sqlalchemy.sql import func
# from sqlalchemy import DateTime

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ruc = db.Column(db.CHAR(11), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    sunat_status = db.Column(db.BOOLEAN, nullable=False, default=True)

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())
    
    establishments = db.relationship('Establishment', backref='company', lazy='dynamic')

    def __init__(self, ruc, name, sunat_status):
        self.ruc = ruc
        self.name = name
        self.sunat_status = sunat_status