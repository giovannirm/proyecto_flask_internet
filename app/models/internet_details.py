from app import db

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