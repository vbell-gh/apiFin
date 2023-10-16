
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime

class CounterPartiesMain(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vatid: str
    country: str 
    company_id: int
    bank_account: str
    company_name_cyrilic: str = Field(index=True)
    company_name_latin: str = Field(index=True)
    address: str

class CounterpartiesAttribs(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, foreign_key="counterpartiesmain.id")
    is_client: bool
    client_is_due: bool
    client_due_days: Optional[int]
    is_vendor: bool
    vendor_is_due: bool
    vendor_due_days: Optional[int]
    is_active: Optional[bool]
    date_deactivaion: Optional[datetime]
    date_created: datetime
    main_contact_name: Optional[str]
    main_contact_email: Optional[str]
    main_contact_phone: Optional[str]
    fin_contact_name: Optional[str]
    fin_contact_email: Optional[str]
    fin_contact_phone: Optional[str]
    upload_one_name: Optional[str]
    upload_one_file: Optional[str] # file path should be here, not the file itself
    upload_two_name: Optional[str]
    upload_two_file: Optional[str]
    upload_three_name: Optional[str]
    upload_three_file: Optional[str]
    # creator_id: Optional[str] = Field(default=None, foreign_key="users.id")

def create_db_tables(engine):
    SQLModel.metadata.create_all(engine)