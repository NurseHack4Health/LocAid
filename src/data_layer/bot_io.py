from pydantic import BaseModel
from typing import Optional, List


class UserInput(BaseModel):
    """
    User's input text model
    """
    user_id: Optional[str]
    text: str


class ItemRequest(BaseModel):
    id: Optional[str]
    name: Optional[str]
    quantity: int


class RequestInput(BaseModel):
    """
    User's item request
    """
    hospital_id: str
    items: List[ItemRequest]


class OrderInput(BaseModel):
    """
    User's order
    """
    id: str
    user_id: str
    from_hospital_id: Optional[str]
    to_hospital_id: str
    items: List[ItemRequest]
    emergency: Optional[bool]
    approved: Optional[bool]
    processed: Optional[bool]
