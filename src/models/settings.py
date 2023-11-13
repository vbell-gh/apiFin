from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarative class for all models."""

    __abstract__ = True


class DocumentTypes(Base):
    """DocumentTypes This class is used to define the document types that are used in the system.
    processing function selects which function processes the document and how it is posted.
    Doc_abbreviation is used to identify the document type in the system, can be used to identify what the user selects.
    The following processing functions will be predefined:
    - SSR (Service sales rows) - used for service sales where each line is separate service. These are recoded in the service revenue table in db.
    - GSR (Good sales rows) - used for goods sales where each line is separate item. These are recoded in the goods revenue table in db. Additionally triggers goods movement and COGS postins.
    - DRN / CRN (Debit / Credit note) - used for debit and credit notes. These are recoded in the AR transactions table in db.
    - NVD (Non vat document) - used for non vat documents. These are recoded in the AR transactions table in db, however have no VAT effect (e.g. guaranes, penalties, as applicable)
    """

    __tablename__ = "document_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    doc_abbreviation: Mapped[str]
    name: Mapped[str]
    processing_func: Mapped[str]
    desctiption: Mapped[Optional[str]]
    counter: Mapped[Optional[int]]  # this is the counter for AR types of documents


class TaxCodes(Base):
    __tablename__ = "tax_codes"
    id: Mapped[int] = mapped_column(primary_key=True)
    tax_code_abriviation: Mapped[str]
    name: Mapped[str]
    description: Mapped[Optional[str]]


class Logs(Base):  # idea for now python loggin module is enough
    __tablename__ = "logs"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created: Mapped[datetime]
    operation_id: Mapped[int] = mapped_column(ForeignKey("gl_transactions.id"))


class GeneralSettings(Base):  # for now can be a simple json file
    __tablename__ = "app_settings"
    id: Mapped[int] = mapped_column(primary_key=True)
    abbreviation: Mapped[str]
    name: Mapped[str]
    value: Mapped[str]
    description: Mapped[Optional[str]]


# Add currency table
