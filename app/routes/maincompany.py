from fastapi import APIRouter

from app.schemas.schemas import CompanySchema
from app.models.models import Company


routercompany = APIRouter(prefix="/companies")

@routercompany.get('/fetchall-companies')
def view_companies():
    companies = Company.query.all()
    return companies