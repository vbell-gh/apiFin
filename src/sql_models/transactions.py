from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarative class for all models."""
    __abstract__ = True


class GLTransactions(Base):
    """GLTransactions All movements of the general ledger are recorded through this table.
    document_refference: is a polimorfic reference to the document that originated the transaction.
    type_of_operation: is a string that indicates the type of operation that originated the transaction, 
    based on which the document that originated the transaction can be identified.
    """
    __tablename__ = 'gl_transactions'
    id: Mapped[int] = mapped_column(primary_key=True)
    document_refference: Mapped[int]
    type_of_operation: Mapped[str]
    account_no: Mapped[int] = mapped_column(
        ForeignKey("gl_accounts.account_code"),)
    amount: Mapped[float]
    currency: Mapped[str]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.document_refference!r}"


class InventoryMovement(Base):
    """IntenotryMovements All movements of invenotry are recorded through this table.
    Based on which COGS is calculated, inventory balances and availability.
    """
    __tablename__ = 'inventory_movements'
    id: Mapped[int] = mapped_column(primary_key=True)
    # polymorfic reference to the document that originated the transaction.
    document_refference: Mapped[int]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"),)
    type_of_operation: Mapped[str]  # type of movement
    quantity: Mapped[float]
    unit_price: Mapped[float]
    total_amount: Mapped[float]
    currency: Mapped[str]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.document_refference!r}"


class GoodsSales(Base):
    """GoodsSales: All sale of goods recoded here.
    """
    __tablename__ = 'goods_sales'
    id: Mapped[int] = mapped_column(primary_key=True)
    document_refference: Mapped[int] = mapped_column(
        ForeignKey("ar_transactions.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    type_of_operation: Mapped[str]
    unit_price: Mapped[float]
    quantity: Mapped[float]
    amount: Mapped[float]
    currency: Mapped[str]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.document_refference!r}"


class ServicesSales(Base):
    """ServicesSales All services sold are registered here.
    """
    __tablename__ = 'services_sales'
    id: Mapped[int] = mapped_column(primary_key=True)
    document_refference: Mapped[int] = mapped_column(
        ForeignKey("ar_transactions.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    type_of_operation: Mapped[str]
    unit_price: Mapped[float]
    quantity: Mapped[float]
    amount: Mapped[float]
    currency: Mapped[str]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.document_refference!r}"


class ARTransactions(Base):
    """ARTransactions All issued invoices are recorded through this table.
    intranl_doc_ref: are the intenally generated document numbers for invoices/credit notes, etc.
    Balances as at certain date are calculated based on this table.
    """
    __tablename__ = 'ar_transactions'
    # polimorfic refence to gl_transactions.document_refference
    id: Mapped[int] = mapped_column(primary_key=True)
    so_id: Mapped[int] = mapped_column(ForeignKey("sales_orders.id"),)
    internal_doc_ref: Mapped[int]  # internal document refference
    document_type: Mapped[str]
    date_posted: Mapped[datetime]
    document_date: Mapped[datetime]
    days_due: Mapped[int]
    net_amount: Mapped[float]
    currency: Mapped[str]
    gross_amount: Mapped[float]
    tax_amount: Mapped[float]
    c_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    crearing_date: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} internal_doc_ref: {self.internal_doc_ref!r}"


class APTransactions(Base):
    """APTransactions All received invoices are recorded through this table.
    intranl_doc_ref: are the external vendor document numbers for invoices/credit notes, etc.
    Balances as at certain date are calculated based on this table.
    """
    __tablename__ = 'ap_transactions'
    # polimorfic refence to gl_transactions.document_refference
    id: Mapped[int] = mapped_column(primary_key=True)
    document_type: Mapped[str]
    external_doc_ref: Mapped[int]  # external document refference
    date_posted: Mapped[datetime]
    document_date: Mapped[datetime]
    days_due: Mapped[int]
    net_amount: Mapped[float]
    currency: Mapped[str]
    gross_amount: Mapped[float]
    tax_amount: Mapped[float]
    c_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))
    clearing_date: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} external_doc_ref: {self.external_doc_ref!r}"


class BankTransactions(Base):
    """BankTransactions All bank movements are recoded here.
    """
    # polimorfic refence to gl_transactions.document_refference
    id: Mapped[int] = mapped_column(primary_key=True)
    ref_no: Mapped[int]
    amount: Mapped[float]
    currency: Mapped[str]
    movement_type: Mapped[str]
    account_id: Mapped[int] = mapped_column(
        ForeignKey("gl_accounts.account_code"))

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} ref_no: {self.ref_no!r}"
