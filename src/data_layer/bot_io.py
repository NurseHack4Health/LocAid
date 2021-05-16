from pydantic import BaseModel
from typing import Optional, List


class UserInput(BaseModel):
    """
    User's input text model
    """
    user_id: Optional[str]
    text: str


class ItemRequest(BaseModel):
    name: str
    quantity: int


class RequestInput(BaseModel):
    """
    User's item request
    """
    hospital_id: str
    items: List[ItemRequest]


