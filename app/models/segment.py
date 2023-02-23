from db import db

class Segment(db.Model):
    __tablename__ = 'segments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    establishments_segment = db.relationship('EstablishmentSegment', backref='segment', lazy='dynamic')

    def __init__(self, name):
        self.name = name