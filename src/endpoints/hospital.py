import sqlalchemy
from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.db_connector import get_db
from src.schemas.hospital import HospitalCreate
from src.models.hospital import HospitalModel
from fastapi import APIRouter
router = APIRouter()


@router.get("/hospital/id/{hospital_id}")
def get_one_hospital_by_id(hospital_id: str, db: Session = Depends(get_db)):
    """
    GET one hospital by ID
    :param hospital_id: Hospital ID to get
    :param db: DB session
    :return: Retrieved hospital entry
    """
    try:
        hospital = db.query(HospitalModel).filter(HospitalModel.id == hospital_id).one()
        return {"id": str(hospital.id), "name": hospital.name}
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{hospital_id} does not exist")


@router.post("/hospital")
def post_one_hospital(hospital: HospitalCreate, db: Session = Depends(get_db)):
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

