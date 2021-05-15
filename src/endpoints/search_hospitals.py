from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.bot_io import RequestInput
from src.data_layer.db_connector import get_db
from src.data_layer.item import search_items_on_quantity
from fastapi import APIRouter
router = APIRouter()


@router.post("/search_hospitals")
def request_item(requested_items: RequestInput, db: Session = Depends(get_db)):
    """
    Receive item request, return the top 3 nearest hospitals which satisfies the condition
    """
    # Get condition
    available_items_list = search_items_on_quantity(requested_items, db)
    return available_items_list

