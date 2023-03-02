from app.models import Establishment
from app import ma

class EstablishmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'company_id', 'department_id')
        model = Establishment
        exclude = ('company_id', 'department_id',)

establishment_schema = EstablishmentSchema()
establishments_schema = EstablishmentSchema(many=True)