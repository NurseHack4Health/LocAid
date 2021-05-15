import datetime
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: Optional[str]
    name: str
    hospital_id: str
    expiry_date: Optional[datetime.date]
    quantities: int
    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    name: str
    hospital_id: str
    quantities: int
