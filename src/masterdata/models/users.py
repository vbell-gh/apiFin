from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class User(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    fullname: str
    email: str
    role_id: int = Field(foreign_key="roles.id")
    user_created: datetime
    
class Roles(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str
    description: str

