from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarative class for all models."""

    __abstract__ = True


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    fullname: Mapped[str]
    email: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    def __repr__(self) -> str:
        return f"User id: {self.id!r} username: {self.username!r}"


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str]
    description: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"Role id: {self.id!r} role_name: {self.role_name!r}"


class GLAccountsMD(Base):
    __tablename__ = "gl_accounts_md"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int]
    name: Mapped[str]
    type: Mapped[str]
    category: Mapped[Optional[str]]
    subcategory: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    status: Mapped[str]

    def __repr__(self) -> str:
        return f"GLAccount id: {self.id!r} code: {self.code!r} name: {self.name!r}"


class IvenotriesMD(Base):
    __tablename__ = "invenotries_md"
    id: Mapped[int] = mapped_column(primary_key=True)
    material_code: Mapped[str]
    name: Mapped[str]
    description: Mapped[Optional[str]]
    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("inv_cat_atributes.id")
    )
    category: Mapped[Optional[str]]
    sub_category: Mapped[Optional[str]]
    unit_of_measure: Mapped[Optional[str]]
    barcode: Mapped[Optional[str]]
    is_active: Mapped[Optional[bool]]
    vendor_code: Mapped[Optional[int]] = mapped_column(ForeignKey("vendors_md.id"))
    date_created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Inventory id: {self.id!r} name: {self.name!r}"


class InvenotriesAtributes(Base):
    __tablename__ = "invenotries_md_attribs"
    id: Mapped[int] = mapped_column(primary_key=True)
    i_id: Mapped[int] = mapped_column(ForeignKey("invenotries_md.id"))
    customs_code: Mapped[Optional[int]]
    customs_description: Mapped[Optional[str]]
    main_unit: Mapped[Optional[str]]
    net_weight: Mapped[Optional[float]]
    gross_weight: Mapped[Optional[float]]
    height: Mapped[Optional[float]]
    width: Mapped[Optional[float]]
    depth: Mapped[Optional[float]]
    # add here connection to warehouse table
    storage_location: Mapped[Optional[str]]
    photo_1_location: Mapped[Optional[str]]
    photo_2_location: Mapped[Optional[str]]
    photo_3_location: Mapped[Optional[str]]
    photo_4_location: Mapped[Optional[str]]


class InvenotryCategoryAtributes(Base):
    __tablename__ = "inv_cat_atributes"
    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str]
    category_description: Mapped[Optional[str]]
    revenue_account: Mapped[Optional[int]] = mapped_column(
        ForeignKey("gl_accounts_md.id")
    )
    cogs_account: Mapped[Optional[int]] = mapped_column(ForeignKey("gl_accounts_md.id"))


class VendorsMasterData(Base):
    __tablename__ = "vendors_md"
    id: Mapped[int] = mapped_column(primary_key=True)
    vatid: Mapped[str]
    country: Mapped[str]
    company_id: Mapped[str]
    bank_account: Mapped[Optional[str]]
    company_name_cyrilic: Mapped[Optional[str]]
    company_name_latin: Mapped[str]
    address: Mapped[str]

    def __repr__(self) -> str:
        return f"Vendor id: {self.id!r} company_name_latin: {self.company_name_latin!r}"


class ClientsMasterData(Base):
    __tablename__ = "clients_md"
    id: Mapped[int] = mapped_column(primary_key=True)
    vatid: Mapped[str]
    country: Mapped[str]
    company_id: Mapped[str]
    bank_account: Mapped[Optional[str]]
    company_name_cyrilic: Mapped[Optional[str]]
    company_name_latin: Mapped[str]
    address: Mapped[str]

    def __repr__(self) -> str:
        return f"Client id: {self.id!r} company_name_latin: {self.company_name_latin!r}"


class ClientsMDAtribs(Base):
    __tablename__ = "clients_md_attribs"
    id: Mapped[int] = mapped_column(primary_key=True)
    c_id: Mapped[int] = mapped_column(ForeignKey("clients_md.id"))
    client_is_due: Mapped[bool]
    client_due_days: Mapped[Optional[int]]
    is_active: Mapped[Optional[bool]]
    main_contact_name: Mapped[Optional[str]]
    main_contact_email: Mapped[Optional[str]]
    main_contact_phone: Mapped[Optional[str]]
    fin_contact_name: Mapped[Optional[str]]
    fin_contact_email: Mapped[Optional[str]]
    fin_contact_phone: Mapped[Optional[str]]
    upload_one_name: Mapped[Optional[str]]
    upload_one_file: Mapped[Optional[str]]  # file path
    upload_two_name: Mapped[Optional[str]]
    upload_two_file: Mapped[Optional[str]]
    upload_three_name: Mapped[Optional[str]]
    upload_three_file: Mapped[Optional[str]]


class VendorMDAtribs(Base):
    __tablename__ = "vendor_md_attribs"
    id: Mapped[int] = mapped_column(primary_key=True)
    c_id: Mapped[int] = mapped_column(ForeignKey("vendors_md.id"))
    vendor_is_due: Mapped[bool]
    vendor_due_days: Mapped[Optional[int]]
    is_active: Mapped[Optional[bool]]
    main_contact_name: Mapped[Optional[str]]
    main_contact_email: Mapped[Optional[str]]
    main_contact_phone: Mapped[Optional[str]]
    fin_contact_name: Mapped[Optional[str]]
    fin_contact_email: Mapped[Optional[str]]
    fin_contact_phone: Mapped[Optional[str]]
    upload_one_name: Mapped[Optional[str]]
    upload_one_file: Mapped[Optional[str]]  # file path
    upload_two_name: Mapped[Optional[str]]
    upload_two_file: Mapped[Optional[str]]
    upload_three_name: Mapped[Optional[str]]
    upload_three_file: Mapped[Optional[str]]
