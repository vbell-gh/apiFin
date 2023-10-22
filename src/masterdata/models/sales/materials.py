from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class InvenotriesMasterData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    material_code: str = Field(index=True)
    name: str = Field(index=True)
    description: Optional[str]
    category: Optional[str]
    sub_category: Optional[str]
    unit_of_measure: Optional[str]
    barcode: Optional[str]
    default_sale_price: Optional[float]
    default_pruchase_price: Optional[float]
    creator_id: Optional[int] = Field(default=None, foreign_key="users.id")
    is_active: Optional[bool]
    vendor_code: Optional[int] = Field(foreign_key="counterpartiesmain.id")
    date_created: datetime


class InvenotriesAtributes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    i_id: int = Field(foreign_key="invenotriesmasterdata.id")
    customs_code: Optional[int]
    customs_description: Optional[str]
    main_unit: Optional[str]
    net_weight: Optional[float]
    gross_weight: Optional[float]
    height: Optional[float]
    width: Optional[float]
    depth: Optional[float]
    storage_location: Optional[str]  # add here connection to warehouse table
    photo_1_location: Optional[str]
    photo_2_location: Optional[str]
    photo_3_location: Optional[str]
    photo_4_location: Optional[str]
