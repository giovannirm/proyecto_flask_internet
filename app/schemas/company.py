from app.models import Company
from app import ma

class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'ruc', 'name', 'sunat_status', 'created_at', 'updated_at')
        model = Company

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)