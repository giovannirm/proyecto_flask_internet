from app.db import db
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import DateTime

# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ruc = db.Column(db.String(11), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)

    created_at_a = db.Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at_a = db.Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    
    departments = db.relationship('Departament', secondary='company_department')

class Departament(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    companies = db.relationship('Company', secondary='company_department')

    def __init__(self, name):
        self.name = name

class CompanyDepartment(db.Model):
    __tablename__ = 'company_department'
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), primary_key=True)

class Segments(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    speed_ranges = db.relationship('SpeedRange', backref='technologies', lazy='dynamic')

    def __init__(self, name):
        self.name = name

class SpeedRange(db.Model):
    __tablename__ = 'speed_ranges'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    technology_id = db.Column(db.Integer, db.ForeignKey('technologies.id'))
    
    def __init__(self, name, technology_id):
        self.name = name
        self.technology_id = technology_id