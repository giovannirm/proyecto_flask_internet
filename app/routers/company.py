from fastapi import APIRouter

from app.schemas.schemas import CompanySchema
from app.models.models import Company


company = APIRouter(prefix="/companies")

@company.get('/fetchall-companies')
def view_companies():
    companies = Company.query.all()
    return companies

# @app.get("/employee/{id}")
# def home(id: int):
#     return {"id": id}