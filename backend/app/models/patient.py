from sqlalchemy import Column, Integer, String, Float, Date
from ..database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    height = Column(Float)
    weight = Column(Float)
