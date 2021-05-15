from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.db_connector import get_db
from src.schemas.item import ItemCreate
from src.models.item import ItemModel
from fastapi import APIRouter
router = APIRouter()


@router.post("/item")
def post_one_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    POST one item
    It reads parameters from the request field and add missing fields from default values defined in the model
    :param item: item class that contains all columns in the table
    :param db: DB session
    :return: Created item entry
    """
    item = ItemModel(**item.dict())

    # Commit to DB
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"id": str(item.id),
            "name": item.name,
            "quantities": item.quantities}

