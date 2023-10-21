from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class GLAccounts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account_code: int = Field(index=True)
    account_name: str
    account_type: str
    account_category: Optional[str]
    account_subcategory: Optional[str]
    account_description: Optional[str]
    account_status: str
    account_created: datetime
    account_creator: int = Field(foreign_key="users.id")