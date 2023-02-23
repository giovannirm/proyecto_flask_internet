from db import db

class Departament(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    establishments = db.relationship('Establishment', backref='department', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name