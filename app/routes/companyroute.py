from flask import Blueprint, jsonify

from app.models import Company
from app.schemas import companies_schema

company = Blueprint('company', __name__)

@company.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()

    if companies:
        return companies_schema.dump(companies)
    
    return jsonify({'message':'No hay compañías'})