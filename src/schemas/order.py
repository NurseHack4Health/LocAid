import datetime
from pydantic import BaseModel
from typing import Optional


class Order(BaseModel):
    id: Optional[str]
    user_id: str
    from_hospital_id: Optional[str]
    to_hospital_id: str
    item_id: str
    emergency: Optional[bool]
    created_at: Optional[bool]
    approved: Optional[bool]
    processed: Optional[bool]
    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    user_id: str
    from_hospital_id: Optional[str]
    to_hospital_id: str
    item_id: str
    emergency: Optional[bool]
    created_at: Optional[bool]
    approved: Optional[bool]
    processed: Optional[bool]
