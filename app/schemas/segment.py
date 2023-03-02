from app.models import Segment
from app import ma

class SegmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Segment

segment_schema = SegmentSchema()
segments_schema = SegmentSchema(many=True)