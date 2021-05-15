from pydantic import BaseModel
from typing import Optional


class Hospital(BaseModel):
    id: Optional[str]
    name: str
    postcode: str
    longitude: Optional[float]
    latitude: Optional[float]

    class Config:
        orm_mode = True


class HospitalCreate(BaseModel):
    name: str
    postcode: str
    longitude: Optional[float]
    latitude: Optional[float]
