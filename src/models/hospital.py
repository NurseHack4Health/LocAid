import uuid
from src.data_layer.db_connector import Base
from sqlalchemy import Column, VARCHAR, FLOAT
from sqlalchemy.dialects.postgresql import UUID


class HospitalModel(Base):
    """
    Define Hospital database table ORM model
    """
    __tablename__ = "hospital"

    # Register columns
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True, index=True)
    name = Column(VARCHAR, unique=False, index=True)
    postcode = Column(VARCHAR, unique=False, index=True)
    longitude = Column(FLOAT, unique=False, index=True)
    latitude = Column(FLOAT, unique=False, index=True)
