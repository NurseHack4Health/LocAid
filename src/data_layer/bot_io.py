from pydantic import BaseModel
from typing import Optional


class UserInput(BaseModel):
    """
    User's input text model
    """
    user_id: Optional[str]
    text: str
