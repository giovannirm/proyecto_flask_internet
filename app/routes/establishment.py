from flask import Blueprint, jsonify

from app.models import Company, Departament, Establishment
from app.schemas import company_schema, department_schema

establishment = Blueprint('establishment', __name__)

# Endpoint para ver las sedes que existen
@establishment.route('/', methods=['GET'])
def get_establishments():
    establishments = Establishment.query.all()
    result = []
    for establishment in establishments:
        company = Company.query.filter_by(id=establishment.company_id).first()
        department = Departament.query.filter_by(id=establishment.department_id).first()
        
        result.append({
            "establishment": establishment.id,
            "company": company_schema.dump(company),
            "department": department_schema.dump(department)
        })
    if result != []:
        return result
        
    return jsonify({'message':'No hay sedes disponibles'})