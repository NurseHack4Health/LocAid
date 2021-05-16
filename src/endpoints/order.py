import sqlalchemy
from fastapi import Depends
from sqlalchemy.orm import Session
from src.data_layer.bot_io import OrderInput
from src.data_layer.db_connector import get_db
from src.models.order import OrderModel
from fastapi import APIRouter
router = APIRouter()


@router.post("/order")
def get_order_by_hospital_id(hospital_id: str, db: Session = Depends(get_db)):
    """
    Create order by hospital ID, items and emergency
    """
    # Create OrderModel per item
    order_item_list = []
    for item in order.items:
        order = {"user_id": order.user_id,
                 "to_hospital_id": order.to_hospital_id,
                 "item_id": item.id,
                 "emergency": order.emergency}
        order_item_list.extend([OrderModel(**order) for i in range(item.quantity)])

    for order_model in order_item_list:
        # Commit to DB
        db.add(order_model)
        db.commit()
        db.refresh(order_model)
    return order_item_list


@router.post("/order")
def create_order(order: OrderInput, db: Session = Depends(get_db)):
    """
    Create order by hospital ID, items and emergency
    """
    # Create OrderModel per item
    order_item_list = []
    for item in order.items:
        order = {"user_id": order.user_id,
                 "to_hospital_id": order.to_hospital_id,
                 "item_id": item.id,
                 "emergency": order.emergency}
        order_item_list.extend([OrderModel(**order) for i in range(item.quantity)])

    for order_model in order_item_list:
        # Commit to DB
        db.add(order_model)
        db.commit()
        db.refresh(order_model)
    return order_item_list


@router.put("/order")
def put_one_order(order_model: OrderInput, db: Session = Depends(get_db)):
    """
    Update one order
    It reads parameters from the request field and update finds the entry and update it
    :param order_model: OrderModel class that contains requested field to update
    :param db: DB session
    :return: Updated order
    """
    try:
        # Get audio_format by ID
        order_to_put = db.query(OrderModel).filter(OrderModel.id == order_model.id).one()

        # Update model class variable for requested fields
        for var, value in vars(order_model).items():
            setattr(order_to_put, var, value) if value else None

        # Commit to DB
        db.add(order_to_put)
        db.commit()
        db.refresh(order_to_put)
        return {"id": str(order_to_put.id), "processed": order_to_put.processed, "approved": order_to_put.approved}
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{order_model.id} does not exist")
