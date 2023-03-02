from app.models import Technology
from app import ma

class TechnologySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Technology

technology_schema = TechnologySchema()
technologies_schema = TechnologySchema(many=True)