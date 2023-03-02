from app.models import Departament
from app import ma

class DepartamentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = Departament

department_schema = DepartamentSchema()
departments_schema = DepartamentSchema(many=True)