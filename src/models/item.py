import uuid
from src.data_layer.db_connector import Base
from sqlalchemy import Column, VARCHAR, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID


class ItemModel(Base):
    """
    Define Item database table ORM model
    """
    __tablename__ = "item"

    # Register columns
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True, index=True)
    name = Column(VARCHAR, unique=False, index=True)
    hospital_id = Column(UUID(as_uuid=True), index=True)
    expiry_date = Column(DateTime, index=True)
    quantities = Column(Integer)
