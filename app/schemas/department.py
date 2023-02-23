from db import ma
from app.models.department import Departament

class DepartamentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Departament

department_schema = DepartamentSchema()
departments_schema = DepartamentSchema(many=True)