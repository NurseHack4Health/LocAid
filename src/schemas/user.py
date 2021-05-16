from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
