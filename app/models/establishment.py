from app import db

class Establishment(db.Model):
    __tablename__ = 'establishments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    establishments_segment = db.relationship('EstablishmentSegment', backref='establishment', lazy='dynamic')

    def __init__(self, company_id, department_id):
        self.company_id = company_id
        self.department_id = department_id