from typing import List
from src.data_layer.bot_io import RequestInput
from src.data_layer.db_tables import Item, Hospital


def search_items_on_quantity(request_input: RequestInput, db_session) -> List[Hospital]:
    """
    Search hospitals which has requested items
    :param request_input: RequestInput class
    :param db_session: DB session
    :return: List of Hospital classes
    """
    # Placeholder
    queried_hospitals = []

    hospital_id = request_input.hospital_id
    request_dict = dict(request_input)
    # Search hospital has requested items
    for item in request_dict['items']:
        item_dict = dict(item)
        queried_hospitals = db_session.query(Hospital).filter(Item.name == item_dict['name'],
                                                              Item.quantities >= item_dict['quantity'],
                                                              Item.hospital_id != hospital_id)\
            .join(Item, Hospital.id == Item.hospital_id).all()

    return queried_hospitals
