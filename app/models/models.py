from app.db import db
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import DateTime

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

class Departament(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    establishments = db.relationship('Establishment', backref='department', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name

class Establishment(db.Model):
    __tablename__ = 'establishments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    establishments_segment = db.relationship('EstablishmentSegment', backref='establishment', lazy='dynamic')

    def __init__(self, company_id, department_id):
        self.company_id = company_id
        self.department_id = department_id

class Segment(db.Model):
    __tablename__ = 'segments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    establishments_segment = db.relationship('EstablishmentSegment', backref='segment', lazy='dynamic')

    def __init__(self, name):
        self.name = name

class EstablishmentSegment(db.Model):
    __tablename__ = 'establishment_segment'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishments.id'), nullable=False)
    segment_id = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable=False)
    internet_details = db.relationship('InternetDetails', backref='establishment_segment', lazy='dynamic')

    def __init__(self, establishment_id, segment_id):
        self.establishment_id = establishment_id
        self.segment_id = segment_id

class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    internet_details = db.relationship('InternetDetails', backref='technology', lazy='dynamic')

    def __init__(self, name):
        self.name = name

class SpeedRange(db.Model):
    __tablename__ = 'speed_ranges'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    internet_details = db.relationship('InternetDetails', backref='speed_range', lazy='dynamic')

    def __init__(self, name):
        self.name = name

class InternetDetails(db.Model):
    __tablename__ = 'internet_details'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    establishment_segment_id = db.Column(db.Integer, db.ForeignKey('establishment_segment.id'), nullable=False)
    technology_id = db.Column(db.Integer, db.ForeignKey('technologies.id'), nullable=False)
    speed_range_id = db.Column(db.Integer, db.ForeignKey('speed_ranges.id'), nullable=True)

    def __init__(self, establishment_segment_id, technology_id, speed_range_id):
        self.establishment_segment_id = establishment_segment_id
        self.technology_id = technology_id
        self.speed_range_id = speed_range_id