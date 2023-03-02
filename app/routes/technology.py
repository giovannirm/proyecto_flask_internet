from flask import Blueprint, jsonify

from app.models import Technology
from app.schemas import technology_schema, technologies_schema

technology = Blueprint('technology', __name__)

# Endpoint para ver las tecnologías que existen 
@technology.route('/', methods=['GET'])
def get_companies():
    technologies = Technology.query.all()

    if technologies:
        return technologies_schema.dump(technologies)
    
    return jsonify({'message':'No hay compañías'})

# Endpoint para ver las tecnologías por id
@technology.route('/<id>', methods=['GET'])
def view_technology(id):
    technology = Technology.query.get(id)

    if technology:
        return technology_schema.dump(technology)
    
    return jsonify({'message':'No hay tecnologías'})