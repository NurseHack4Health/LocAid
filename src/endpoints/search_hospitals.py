from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.bot_io import RequestInput
from src.data_layer.db_connector import get_db
from src.logic_layer.search_hospitals import search_hospitals
from fastapi import APIRouter
router = APIRouter()


@router.post("/search_hospitals")
def search_hospitals_with_requested_items(request_input: RequestInput, db: Session = Depends(get_db)):
    """
    Receive item request, return the top 3 nearest hospitals which satisfies the condition
    """
    return search_hospitals(request_input, db)
