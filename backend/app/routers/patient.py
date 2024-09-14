from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models import patient as patient_model
from ..schemas import patient as patient_schema

router = APIRouter()

@router.post("/patients/", response_model=patient_schema.Patient)
def create_patient(patient: patient_schema.PatientCreate, db: Session = Depends(get_db)):
    return patient_model.create_patient(db=db, patient=patient)

@router.get("/patients/", response_model=list[patient_schema.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = patient_model.get_patients(db, skip=skip, limit=limit)
    return patients

@router.get("/patients/{patient_id}", response_model=patient_schema.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = patient_model.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.put("/patients/{patient_id}", response_model=patient_schema.Patient)
def update_patient(patient_id: int, patient: patient_schema.PatientUpdate, db: Session = Depends(get_db)):
    return patient_model.update_patient(db=db, patient_id=patient_id, patient=patient)
