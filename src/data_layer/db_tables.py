# coding: utf-8
import os
import uuid
from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    PrimaryKeyConstraint,
    DateTime,
    Boolean
)
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

BaseTable = declarative_base()


class Hospital(BaseTable):
    __tablename__ = "hospital"
    __table_args__ = {"schema": os.environ.get('SCHEMA_NAME')}

    id = Column(
        UUID,
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    name = Column(String(200))
    postcode = Column(String(200))
    longitude = Column(Float)
    latitude = Column(Float)
    PrimaryKeyConstraint(id, name="PK_hospital_id")


class User(BaseTable):
    __tablename__ = "user"
    __table_args__ = {"schema": os.environ.get('SCHEMA_NAME')}

    id = Column(
        UUID,
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    name = Column(String(200))
    email = Column(String(200))
    password = Column(String(200))
    hospital_id = Column(UUID, ForeignKey("locaid.hospital.id", name="FK_user_hospital_id_hospital_id"))
    PrimaryKeyConstraint(id, name="PK_user_id")


class Item(BaseTable):
    __tablename__ = "item"
    __table_args__ = {"schema": os.environ.get('SCHEMA_NAME')}

    id = Column(
        UUID,
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    name = Column(String(200))
    hospital_id = Column(UUID, ForeignKey("locaid.hospital.id", name="FK_item_hospital_id_hospital_id"))
    quantities = Column(Integer)
    expiry_date = Column(UUID)
    PrimaryKeyConstraint(id, name="PK_item_id")


class Order(BaseTable):
    __tablename__ = "order"
    __table_args__ = {"schema": os.environ.get('SCHEMA_NAME')}

    id = Column(
        UUID,
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    user_id = Column(UUID, ForeignKey("locaid.user.id", name="FK_order_user_id_user_id"))
    from_hospital_id = Column(UUID, ForeignKey("locaid.hospital.id", name="FK_order_hospital_id_hospital_id"))
    to_hospital_id = Column(UUID, ForeignKey("locaid.hospital.id", name="FK_order_hospital_id_hospital_id"))
    item_id = Column(UUID, ForeignKey("locaid.item.id", name="FK_order_item_id_item_id"))
    approved = Column(Boolean)
    processed = Column(Boolean)
    emergency = Column(Boolean)
    created_at = Column(DateTime, default=func.now())
    PrimaryKeyConstraint(id, name="PK_order_id")
