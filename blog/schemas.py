from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    content: str
    author: str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None

class BlogResponse(BlogBase):
    id: str = Field(alias="_id")
    created_at: datetime

    class Config:
        populate_by_name = True