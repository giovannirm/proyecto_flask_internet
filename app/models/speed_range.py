from app import db

class SpeedRange(db.Model):
    __tablename__ = 'speed_ranges'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    internet_details = db.relationship('InternetDetail', backref='speed_range', lazy='dynamic')

    def __init__(self, name):
        self.name = name