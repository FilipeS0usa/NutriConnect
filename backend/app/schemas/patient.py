from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    name: str
    email: str
    birth_date: date
    height: float
    weight: float

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True
