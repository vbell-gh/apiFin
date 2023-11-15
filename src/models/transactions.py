from datetime import datetime
from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base


class DocumentsAssociation(Base):
    """DocumentsAssociation Each document that originates a transaction is recorded here
    and references the transaction and respective table
    Accounting documents also originate here, however they don't refer to any ourside transaction
    """  # This can be replace with polymorphic association

    __tablename__ = "documents_association"
    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    doc_type: Mapped[
        str
    ]  # This is the name of the table that originated the transaction
    doc_sub_type: Mapped[Optional[str]]
    is_accounting_posing: Mapped[bool]

    # Relationships
    gl_transactions: Mapped[List["GLTransactions"]] = relationship(
        back_populates="documents_association"
    )
    ar_transactions: Mapped[Optional["ARTransactions"]] = relationship(
        back_populates="documents_association"
    )
    ap_transactions: Mapped[Optional["APTransactions"]] = relationship(
        back_populates="documents_association"
    )
    bank_transactions: Mapped[Optional["BankTransactions"]] = relationship(
        back_populates="documents_association"
    )

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} doc_type: {self.doc_type!r}"


class GLTransactions(Base):
    """GLTransactions All movements of the general ledger are recorded through this table.
    document_association: is a to helper table that originates the transaction.
    type_of_operation: is a string that indicates the type of operation that originated the transaction,
    based on which the document that originated the transaction can be identified.
    """

    __tablename__ = "gl_transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    doc_id: Mapped[int] = mapped_column(ForeignKey("documents_association.id"))
    account_no: Mapped[int] = mapped_column(ForeignKey("md_gl_accounts.id"))
    type_of_operation: Mapped[str]  # DR or CR
    amount: Mapped[float]
    line_text: Mapped[Optional[str]]
    line_description: Mapped[Optional[str]]
    created: Mapped[datetime]

    documents_association: Mapped["DocumentsAssociation"] = relationship(
        back_populates="gl_transactions"
    )

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_association: {self.type_of_operation!r}"


class ARTransactions(Base):
    """ARTransactions All issued invoices are recorded through this table.
    intranl_doc_ref: are the intenally generated document numbers for invoices/credit notes, etc.
    Balances as at certain date are calculated based on this table.
    """

    __tablename__ = "ar_transactions"
    # polimorfic refence to gl_transactions.document_refference
    id: Mapped[int] = mapped_column(primary_key=True)
    so_id: Mapped[Optional[int]]  # sales order id if applicable
    documents_association_id: Mapped[int] = mapped_column(
        ForeignKey("documents_association.id")
    )
    document_type: Mapped[str]  # mapped to settings
    internal_doc_ref: Mapped[int]  # generated
    date_posted: Mapped[datetime]
    document_date: Mapped[datetime]
    days_due: Mapped[Optional[int]]
    c_id: Mapped[int] = mapped_column(ForeignKey("md_clients.id"))
    tax_code: Mapped[str]  # mapped to settings
    date_closed: Mapped[Optional[datetime]]
    net_amount: Mapped[float]
    tax_amount: Mapped[float]
    gross_amount: Mapped[float]
    currency: Mapped[str]

    goods_sales_lines: Mapped[Optional[List["GoodsSalesLines"]]] = relationship(
        back_populates="ar_transactions"
    )
    services_sales_lines: Mapped[Optional[List["ServicesSalesLines"]]] = relationship(
        back_populates="ar_transactions"
    )
    documents_association: Mapped["DocumentsAssociation"] = relationship(
        back_populates="ar_transactions"
    )

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
    id: Mapped[int] = mapped_column(primary_key=True)
    documents_association_id: Mapped[int] = mapped_column(
        ForeignKey("documents_association.id")
    )
    document_type: Mapped[str] # mapped to settings
    external_doc_ref: Mapped[int]  # external document refference
    date_posted: Mapped[datetime]
    document_date: Mapped[datetime]
    days_due: Mapped[int]
    c_id: Mapped[int] = mapped_column(ForeignKey("md_vendors.id"))
    tax_code: Mapped[str]
    date_closed: Mapped[Optional[datetime]]
    net_amount: Mapped[float]
    tax_amount: Mapped[float]
    gross_amount: Mapped[float]
    currency: Mapped[str]

    documents_association: Mapped["DocumentsAssociation"] = relationship(
        back_populates="ap_transactions"
    )

    def __repr__(self) -> str:
        return (
            f"Transaction id: {self.id!r} external_doc_ref: {self.external_doc_ref!r}"
        )


class BankTransactions(Base):
    """BankTransactions All bank movements are recoded here."""

    __tablename__ = "bank_transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    documents_association_id: Mapped[int] = mapped_column(
        ForeignKey("documents_association.id")
    )
    ref_no: Mapped[int]
    amount: Mapped[float]
    currency: Mapped[str]
    movement_type: Mapped[str]
    account_id: Mapped[int] = mapped_column(ForeignKey("md_gl_accounts.id"))
    
    documents_association: Mapped["DocumentsAssociation"] = relationship(
        back_populates="bank_transactions"
    )

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} ref_no: {self.ref_no!r}"


class GoodsSalesLines(Base):
    """GoodsSales: All sale of goods recoded here."""

    __tablename__ = "goods_sales_lines"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("ar_transactions.id"))
    material_id: Mapped[Optional[int]] = mapped_column(ForeignKey("md_invenotries.id"))
    account_id: Mapped[Optional[int]] = mapped_column(ForeignKey("md_gl_accounts.id"))
    custom_line_name: Mapped[Optional[str]]
    unit_price: Mapped[float]
    quantity: Mapped[float]
    amount: Mapped[float]
    ar_transactions: Mapped["ARTransactions"] = relationship(
        back_populates="goods_sales_lines"
    )

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.amount!r}"


class ServicesSalesLines(Base):
    """ServicesSales All services sold are registered here."""

    __tablename__ = "services_sales_lines"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("ar_transactions.id"))
    service_id: Mapped[Optional[int]] = mapped_column(ForeignKey("md_services.id"))
    account_id: Mapped[Optional[int]] = mapped_column(ForeignKey("md_gl_accounts.id"))
    custom_line_name: Mapped[Optional[str]]
    unit_price: Mapped[float]
    quantity: Mapped[float]
    amount: Mapped[float]
    ar_transactions: Mapped["ARTransactions"] = relationship(
        back_populates="services_sales_lines"
    )

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.amount!r}"


class InventoryMovement(Base):
    """IntenotryMovements All movements of invenotry are recorded through this table.
    Based on which COGS is calculated, inventory balances and availability.
    """

    __tablename__ = "inventory_movements"
    id: Mapped[int] = mapped_column(primary_key=True)
    material_id: Mapped[int] = mapped_column(ForeignKey("md_invenotries.id"))
    document_refference_in: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ap_transactions.id")
    )
    document_refference_out: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ar_transactions.id")
    )
    order_id: Mapped[int]  # order id if applicable
    type_of_operation: Mapped[str]  # type of movement
    quantity: Mapped[float]
    unit_price: Mapped[float]  # only cost of goods sold is recorded here
    total_amount: Mapped[float]
    created: Mapped[datetime]

    def __repr__(self) -> str:
        return f"Transaction id: {self.id!r} document_refference: {self.type_of_operation!r}"
