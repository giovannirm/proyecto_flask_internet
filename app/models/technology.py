from app import db

class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    internet_details = db.relationship('InternetDetails', backref='technology', lazy='dynamic')

    def __init__(self, name):
        self.name = name