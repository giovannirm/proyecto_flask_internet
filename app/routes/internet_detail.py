from flask import Blueprint, jsonify

from app.models import Company
from app.schemas import company_schema, speed_range_schema, technology_schema

internet_detail = Blueprint('internet_detail', __name__)

# Endpoint para ver las tecnologías, velocidad por empresa
@internet_detail.route('/', methods=['GET'])
def get_internet_details():
    companies = Company.query.all()

    result = []
    for company in companies:
        speed_ranges = []
        technologies = []
        for establishment in company.establishments:
            for headquarter in establishment.establishments_segment:
                for detail in headquarter.internet_details:
                    speed_ranges.append(speed_range_schema.dump(detail.speed_range))
                    technologies.append(technology_schema.dump(detail.technology))

        result.append({
            "company": company_schema.dump(company),
            "speed_ranges": speed_ranges,
            "technologies": technologies
        })
    if result != []:
        return result
    
    return jsonify({'message':'No hay detalles de internet'})