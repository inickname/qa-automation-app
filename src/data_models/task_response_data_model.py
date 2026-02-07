from typing import Optional

from pydantic import BaseModel


class Status(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    color: Optional[str] = None
    orderindex: Optional[int] = None
    type: Optional[str] = None


class TaskResponseModel(BaseModel):
    id: Optional[str] = None
    custom_id: Optional[str] = None
    custom_item_id: Optional[int] = None
    name: str
    text_content: Optional[str] = None
    description: str
    status: Optional[Status] = None

    class Config:
        extra = "allow"
