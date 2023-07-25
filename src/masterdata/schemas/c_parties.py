from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CounterpartiesBase(BaseModel):
    vatid: int
    country: str
    company_id: int
    bank_account: str | None
    company_name_cyrilic: str
    company_name_latin: str
    address: str
    is_client: bool | None
    client_is_due: bool | None
    client_due_days: str | None
    is_vendor: bool | None
    vendor_is_due: bool | None
    vendor_due_days: str | None
    main_contact_name: str
    main_contact_email: str
    main_contact_phone: str
    fin_contact_name: str | None
    fin_contact_email: str | None
    fin_contact_phone: str | None
    upload_one_name: str | None
    upload_one_file: bytes | None
    upload_two_name: str | None
    upload_two_file: bytes | None
    upload_three_name: str | None
    upload_three_file: bytes | None
    is_active : bool | None
    date_created : datetime
    date_deactivaion : datetime


