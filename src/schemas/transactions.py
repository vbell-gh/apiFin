from pydantic import BaseModel
from datetime import date


class DocumentsAssociation(BaseModel):
    document_type: str
    document_id: int

    class Config:
        orm_mode = True

class GLTransactions(BaseModel):
    type_of_operation: str
    account_no: int
    amount: float
    currency: str

    class Config:
        orm_mode = True


class InventoryMovements(BaseModel):
    pass


class CouterpartyTransactions(BaseModel):
    counter_party_name: str
    documment_type: str
    documnent_date: date
    due_date: date
    due_days: int
    tax_code: str
    net_amount: float
    tax_amount: float
    gross_amount: float
    currency: str

    class Config:
        orm_mode = True


class DocumentLines(BaseModel):
    id: int
    service_or_product: str
    type_of_operation: str
    unit_price: float
    quantity: float
    amount: float

    class Config:
        orm_mode = True


class ARTransactions(CouterpartyTransactions):
    document_lines: list[DocumentLines]


class APTransactions(CouterpartyTransactions):
    extrernal_doc_ref: str
    document_lines: list[DocumentLines]


class DocumentTypes(BaseModel):
    abbreviation: str
    name: str
    description: str

    class Config:
        orm_mode = True
