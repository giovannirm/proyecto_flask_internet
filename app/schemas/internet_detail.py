from db import ma

from app.schemas.company import CompanySchema
from app.schemas.department import DepartamentSchema

from app.models.internet_details import InternetDetails
from app.models.technology import Technology
from app.models.speed_range import SpeedRange
from app.models.establishment_segment import EstablishmentSegment
from app.models.establishment import Establishment
from app.models.segment import Segment

class EstablishmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'company_id', 'department_id')
        model = Establishment

    company_id = ma.Nested(CompanySchema)
    department_id = ma.Nested(DepartamentSchema)

class SegmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Segment

class EstablishmentSegmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'establishment_id', 'segment_id')
        model = EstablishmentSegment

    establishment_id = ma.Nested(EstablishmentSchema)
    segment_id = ma.Nested(SegmentSchema)

class TechnologySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Technology

class SpeedRangeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = SpeedRange

class InternetDetailsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'establishment_segment_id', 'technology_id', 'speed_range_id')
        model = InternetDetails

    establishment_segment_id = ma.Nested(EstablishmentSegmentSchema)
    technology_id = ma.Nested(TechnologySchema)
    speed_range_id = ma.Nested(SpeedRangeSchema)

    _links = ma.Hyperlinks({
        'self': ma.URLFor('est_seg', values=dict(id='<id>')),
    })

establishment_schema = EstablishmentSchema()
establishments_schema = EstablishmentSchema(many=True)

segment_schema = SegmentSchema()
segments_schema = SegmentSchema(many=True)

establishment_segment_schema = EstablishmentSegmentSchema()
establishments_segment_schema = EstablishmentSegmentSchema(many=True)

technology_schema = TechnologySchema()
technologies_schema = TechnologySchema(many=True)

speed_range_schema = SpeedRangeSchema()
speed_ranges_schema = SpeedRangeSchema(many=True)

internet_detail_schema = InternetDetailsSchema()
internet_details_schema = InternetDetailsSchema(many=True)