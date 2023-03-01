from app.models import *
from app import ma

class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'ruc', 'name', 'sunat_status', 'created_at', 'updated_at')
        model = Company

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

class DepartamentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Departament

department_schema = DepartamentSchema()
departments_schema = DepartamentSchema(many=True)

class EstablishmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'company_id', 'department_id')
        model = Establishment
        exclude = ('company_id', 'department_id',)

establishment_schema = EstablishmentSchema()
establishments_schema = EstablishmentSchema(many=True)

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
        model = SpeedRange
        fields = ('id', 'name')



segment_schema = SegmentSchema()
segments_schema = SegmentSchema(many=True)

establishment_segment_schema = EstablishmentSegmentSchema()
establishments_segment_schema = EstablishmentSegmentSchema(many=True)

technology_schema = TechnologySchema()
technologies_schema = TechnologySchema(many=True)


class InternetDetailsSchema(ma.Schema):
    class Meta:
        model = InternetDetails
        fields = ('id', 'establishment_segment_id', 'technology_id', 'speed_range_id')

    establishment_segment_id = ma.Nested(EstablishmentSegmentSchema)
    technology_id = ma.Nested(TechnologySchema)
    speed_range_id = ma.Nested(SpeedRangeSchema)


speed_range_schema = SpeedRangeSchema()
speed_ranges_schema = SpeedRangeSchema(many=True)

internet_detail_schema = InternetDetailsSchema()
internet_details_schema = InternetDetailsSchema(many=True)