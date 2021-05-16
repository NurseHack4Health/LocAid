import uuid
from src.data_layer.db_connector import Base
from sqlalchemy import Column, VARCHAR, FLOAT
from sqlalchemy.dialects.postgresql import UUID


class UserModel(Base):
    """
    Define User database table ORM model
    """
    __tablename__ = "user"

    # Register columns
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True, index=True)
    name = Column(VARCHAR, unique=False, index=True)
    email = Column(VARCHAR, unique=False, index=True)
    password = Column(VARCHAR, unique=False, index=True)
