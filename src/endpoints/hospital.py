from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.db_connector import get_db
from src.schemas.hospital import HospitalCreate
from src.models.hospital import HospitalModel
from fastapi import APIRouter
router = APIRouter()


@router.post("/hospital")
def post_one_organization(hospital: HospitalCreate, db: Session = Depends(get_db)):
    """
    POST one hospital
    It reads parameters from the request field and add missing fields from default values defined in the model
    :param hospital: hospital class that contains all columns in the table
    :param db: DB session
    :return: Created hospital entry
    """
    hospital = HospitalModel(**hospital.dict())

    # Commit to DB
    db.add(hospital)
    db.commit()
    db.refresh(hospital)
    return {"id": str(hospital.id),
            "name": hospital.name}

