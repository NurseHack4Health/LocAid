from src.data_layer.bot_io import RequestInput
from src.data_layer.db_tables import Item, Hospital


def search_items_on_quantity(items_list: RequestInput, db_session):
    items_dict = dict(items_list)
    for item in items_dict['items']:
        item_dict = dict(item)
        queried_items = db_session.query(Hospital).filter(Item.name == item_dict['name'], Item.quantities >= item_dict['quantity']).join(Item, Hospital.id==Item.hospital_id).all()

    # Add filters
    # 1. Exclude own hospital
    # 2. Sort by distance
    return queried_items
