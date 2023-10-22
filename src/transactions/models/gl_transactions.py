from enum import Enum
from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from config import ApiDefault

CURRENCY = ApiDefault().currency


class TypeOfOperation(Enum):
    DEBIT = "debit"
    CREDIT = "credit"


class GLTransactions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    document_reference: Optional[int] = Field(default=None)
    account_no: int = Field(foreign_key="glaccounts.account_code")
    type_of_operation: TypeOfOperation
    ammount: float = Field(default=0.0)
    currency: str = Field(default=CURRENCY)
    created: datetime = Field(default=datetime.now())
