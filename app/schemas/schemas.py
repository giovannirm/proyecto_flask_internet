from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import uuid4 as uuid

class CompanySchema(BaseModel):
    id: Optional[int]
    ruc: str
    name: str
    sunat_status: Optional[bool] = True
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()