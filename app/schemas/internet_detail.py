from app.models import InternetDetail
from app import ma

class InternetDetailSchema(ma.Schema):
    class Meta:
        model = InternetDetail
        fields = ('id', 'establishment_segment_id', 'technology_id', 'speed_range_id')

internet_detail_schema = InternetDetailSchema()
internet_details_schema = InternetDetailSchema(many=True)