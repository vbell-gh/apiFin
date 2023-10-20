from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel



class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    fullname: str
    email: str
    role_id: int = Field(foreign_key="roles.id")
    user_created: datetime


class Roles(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str
    description: str


def create_db_tables(engine):
    SQLModel.metadata.create_all(engine)
