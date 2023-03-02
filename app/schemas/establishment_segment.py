from app.models import EstablishmentSegment
from app import ma
        
class EstablishmentSegmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'establishment_id', 'segment_id')
        model = EstablishmentSegment

establishment_segment_schema = EstablishmentSegmentSchema()
establishments_segment_schema = EstablishmentSegmentSchema(many=True)