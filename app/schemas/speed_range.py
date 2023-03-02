from app.models import SpeedRange
from app import ma

class SpeedRangeSchema(ma.Schema):
    class Meta:
        model = SpeedRange
        fields = ('id', 'name')

speed_range_schema = SpeedRangeSchema()
speed_ranges_schema = SpeedRangeSchema(many=True)