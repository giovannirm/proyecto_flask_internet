from app import db

class EstablishmentSegment(db.Model):
    __tablename__ = 'establishment_segment'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishments.id'), nullable=False)
    segment_id = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable=False)
    internet_details = db.relationship('InternetDetail', backref='establishment_segment', lazy='dynamic')

    def __init__(self, establishment_id, segment_id):
        self.establishment_id = establishment_id
        self.segment_id = segment_id