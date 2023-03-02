from flask import Blueprint, jsonify

from app.models import Departament
from app.schemas import company_schema, department_schema, departments_schema

deparment = Blueprint('deparment', __name__)

# Endpoint para ver las empresas que existen 
@deparment.route('/', methods=['GET'])
def get_companies():
    departments = Departament.query.all()

    if departments:
        return departments_schema.dump(departments)
    
    return jsonify({'message':'No hay departamentos'})

# Endpoint para ver las empresas que se encuentran en cada departamento
@deparment.route('/company/<id>', methods=['GET'])
def view_companies_department(id):
    department = Departament.query.get(id)

    companies = []
    for establishment in department.establishments:
        companies.append(company_schema.dump(establishment.company))

    result = {
        "department": department_schema.dump(department),
        "companies": companies   
    }
    
    if result != []:
        return result
    
    return jsonify({'message':'No hay compañías registradas con el identificador indicado'})