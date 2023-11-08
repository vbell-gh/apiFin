from pydantic import BaseModel


class UserBase(BaseModel):
    """UserBase class for pydantic model"""

    username: str


class UserCreate(UserBase):
    """UserCreate only in creation can be passed password"""

    password: str
    fullname: str
    email: str
    role_id: int


class User(UserBase):
    """User creation class pydantic model"""

    id: int
    fullname: str
    email: str
    role_id: int

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    role_name: str
    description: str


class Role(RoleBase):
    id: int

class GLAccountsMDBase(BaseModel):
    code: int
    name: str
    type: str
    category: str
    subcategory: str
    description: str
    status: str

    class Config:
        orm_mode = True


class InventoryMD(BaseModel):
    material_code: str
    name: str
    description: str
    category: str
    sub_category: str
    unit_of_measure: str
    barcode: str
    is_active: bool
    vendor_name: str
    customs_code: int
    customs_description: str
    main_unit: str
    net_weight: float
    gross_weight: float
    height: float
    width: float
    depth: float
    storage_location: str
    photo_1_location: str
    photo_2_location: str
    photo_3_location: str
    photo_4_location: str

    class Config:
        orm_mode = True


class InvenotryCatAtribs(BaseModel):
    category_name: str
    category_description: str
    revenue_account: int
    cogs_account: int

    class Config:
        orm_mode = True


class CounterPartiesMD(BaseModel):
    vatid: str
    country: str
    company_id: str
    bank_account: str
    company_name_cyrilic: str
    company_name_latin: str
    address: str
    is_active: bool
    main_contact_name: str
    main_contact_email: str
    main_contact_phone: str
    fin_contact_name: str
    fin_contact_email: str
    fin_contact_phone: str
    upload_one_name: str
    upload_one_file: str
    upload_two_name: str
    upload_two_file: str
    upload_three_name: str
    upload_three_file: str

    class Config:
        orm_mode = True


class VendorDetails(CounterPartiesMD):
    vendor_is_due: bool
    due_days: int


class ClientDetails(CounterPartiesMD):
    client_is_due: bool
    due_days: int
