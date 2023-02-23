from db import ma
from app.models.company import Company

class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'ruc', 'name', 'sunat_status', 'created_at', 'updated_at')
        model = Company

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)