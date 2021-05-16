import os
import hashlib
from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.db_connector import get_db
from src.schemas.user import UserCreate
from src.models.user import UserModel
from fastapi import APIRouter
router = APIRouter()


@router.post("/user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create one user
    :param user: UserCreate model
    :param db: DB session
    :return: Created user
    """
    user = UserModel(**user.dict())
    # Hash password
    key = hashlib.pbkdf2_hmac('sha256',
                              user.password.encode('utf-8'),
                              os.urandom(32),  # Salt
                              100000)  # Number of iteration

    # Commit to DB
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": str(user.id),
            "name": user.name}
