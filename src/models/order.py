import uuid
from src.data_layer.db_connector import Base
from sqlalchemy import Column, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func


class OrderModel(Base):
    """
    Define Item database table ORM model
    """
    __tablename__ = "order"

    # Register columns
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), index=True)
    from_hospital_id = Column(UUID(as_uuid=True), index=True)
    to_hospital_id = Column(UUID(as_uuid=True), index=True)
    item_id = Column(UUID(as_uuid=True), index=True)
    emergency = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    approved = Column(Boolean, default=False)
    processed = Column(Boolean, default=False)
