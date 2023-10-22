from typing import Optional
from sqlmodel import Field, SQLModel


class ServicesMasterData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str]
    default_price: Optional[float]
    posting_account: int = Field(foreign_key="accounts.id")
    creator_id: Optional[int] = Field(default=None, foreign_key="users.id")
