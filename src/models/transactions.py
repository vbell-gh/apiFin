from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarative class for all models."""

    __abstract__ = True


class GLTransactions(Base):
    """GLTransactions All movements of the general ledger are recorded through this table.
    document_association: is a to helper table that originates the transaction.
    type_of_operation: is a string that indicates the type of operation that originated the transaction,
    based on which the document that originated the transaction can be identified.
    """

    __tablename__ = "gl_transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_association: Mapped[int] = mapped_column(
        ForeignKey("documents_association.id")
    )
    type_of_operation: Mapped[str]
    account_no: Mapped[int] = mapped_column(ForeignKey("gl_accounts.account_code"))
    amount: Mapped[float]
    currency: Mapped[str]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_association: {self.document_association!r}"


class DocumentsAssociation(Base):
    """DocumentsAssociation Each document that originates a transaction is recorded here
    and references the transaction and respective table"""  # This can be replace with polymorphic association

    __tablename__ = "documents_association"
    id: Mapped[int] = mapped_column(primary_key=True)
    doc_type: Mapped[
        str
    ]  # This is the name of the table that originated the transaction
    doc_sub_type: Mapped[Optional[str]]
    inventory_movement_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("inventory_movements.id")
    )
    ar_document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ar_transactions.id")
    )
    ap_document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ap_transactions.id")
    )
    bank_document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("bank_transactions.id")
    )

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} doc_type: {self.doc_type!r}"


class InventoryMovement(Base):
    """IntenotryMovements All movements of invenotry are recorded through this table.
    Based on which COGS is calculated, inventory balances and availability.
    """

    __tablename__ = "inventory_movements"
    id: Mapped[int] = mapped_column(primary_key=True)
    material_id: Mapped[int] = mapped_column(ForeignKey("invenotries_md.id"))
    document_refference_in: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ap_transactions.id")
    )
    document_refference_out: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ar_transactions.id")
    )
    order_id: Mapped[int]  # order id if applicable
    type_of_operation: Mapped[str]  # type of movement
    quantity: Mapped[float]
    unit_price: Mapped[float]
    total_amount: Mapped[float]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.type_of_operation!r}"


class ARTransactions(Base):
    """ARTransactions All issued invoices are recorded through this table.
    intranl_doc_ref: are the intenally generated document numbers for invoices/credit notes, etc.
    Balances as at certain date are calculated based on this table.
    """

    __tablename__ = "ar_transactions"
    # polimorfic refence to gl_transactions.document_refference
    id: Mapped[int] = mapped_column(primary_key=True)
    so_id: Mapped[int] = mapped_column(
        ForeignKey("sales_orders.id"),
    )
    internal_doc_ref: Mapped[int]  # internal document refference
    document_type: Mapped[str]
    date_posted: Mapped[datetime]
    document_date: Mapped[datetime]
    days_due: Mapped[int]
    c_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    tax_code: Mapped[str]
    date_closed: Mapped[Optional[datetime]]
    net_amount: Mapped[float]
    tax_amount: Mapped[float]
    gross_amount: Mapped[float]
    currency: Mapped[str]

    def __repr__(self) -> str:
        return (
            f"Transaction id: {self.id!r} internal_doc_ref: {self.internal_doc_ref!r}"
        )


class APTransactions(Base):
    """APTransactions All received invoices are recorded through this table.
    intranl_doc_ref: are the external vendor document numbers for invoices/credit notes, etc.
    Balances as at certain date are calculated based on this table.
    """

    __tablename__ = "ap_transactions"
    # polimorfic refence to gl_transactions.document_refference
    id: Mapped[int] = mapped_column(primary_key=True)
    document_type: Mapped[str]
    external_doc_ref: Mapped[int]  # external document refference
    date_posted: Mapped[datetime]
    document_date: Mapped[datetime]
    days_due: Mapped[int]
    c_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))
    tax_code: Mapped[str]
    date_closed: Mapped[Optional[datetime]]
    net_amount: Mapped[float]
    tax_amount: Mapped[float]
    gross_amount: Mapped[float]
    currency: Mapped[str]

    def __repr__(self) -> str:
        return (
            f"Transaction id: {self.id!r} external_doc_ref: {self.external_doc_ref!r}"
        )


class BankTransactions(Base):
    """BankTransactions All bank movements are recoded here."""

    id: Mapped[int] = mapped_column(primary_key=True)
    ref_no: Mapped[int]
    amount: Mapped[float]
    currency: Mapped[str]
    movement_type: Mapped[str]
    account_id: Mapped[int] = mapped_column(ForeignKey("gl_accounts_md.code"))

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} ref_no: {self.ref_no!r}"


class GoodsSalesLines(Base):
    """GoodsSales: All sale of goods recoded here."""

    __tablename__ = "goods_sales_lines"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_refference: Mapped[int] = mapped_column(ForeignKey("ar_transactions.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    type_of_operation: Mapped[str]
    unit_price: Mapped[float]
    quantity: Mapped[float]
    amount: Mapped[float]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.document_refference!r}"


class ServicesSalesLines(Base):
    """ServicesSales All services sold are registered here."""

    __tablename__ = "services_sales_lines"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_refference: Mapped[int] = mapped_column(ForeignKey("ar_transactions.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    type_of_operation: Mapped[str]
    unit_price: Mapped[float]
    quantity: Mapped[float]
    amount: Mapped[float]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.document_refference!r}"
