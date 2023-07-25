from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from typing import Optional
from datetime import datetime


Base = declarative_base()

class CounterpartiesMain(Base):
    __tablename__ = 'counterparties_main'

    id: Mapped[int] = mapped_column(primary_key=True)
    vatid: Mapped[str] = mapped_column(unique=True, nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    company_id: Mapped[int] = mapped_column(
        Integer, unique=True, nullable=False)
    bank_account: Mapped[Optional[str]]
    company_name_cyrilic: Mapped[Optional[str]]
    company_name_latin: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str]

    attributes: Mapped['CounterpartiesAttribs'] = relationship(
        back_populates='counterparties_main')

class CounterpartiesAttribs(Base):
    __tablename__ = 'counterparties_attribs'

    id: Mapped[CounterpartiesMain] = mapped_column(
        ForeignKey('counterparties_main.id'), 
        primary_key=True)
    is_client: Mapped[bool]
    client_is_due: Mapped[Optional[bool]]
    client_due_days: Mapped[Optional[int]]
    is_vendor: Mapped[bool]
    vendor_is_due: Mapped[Optional[bool]]
    vendor_due_days: Mapped[Optional[int]]
    is_active = Column(Boolean, nullable=False)
    date_deactivaion: Mapped[Optional[datetime]]
    date_created: Mapped[datetime]
    main_contact_name: Mapped[Optional[str]]
    main_contact_email: Mapped[Optional[str]]
    main_contact_phone: Mapped[Optional[str]]
    fin_contact_name: Mapped[Optional[str]]
    fin_contact_email: Mapped[Optional[str]]
    fin_contact_phone: Mapped[Optional[str]]
    upload_one_name: Mapped[Optional[str]]
    upload_one_file: Mapped[Optional[str]] # file path should be here, not the file itself
    upload_two_name: Mapped[Optional[str]]
    upload_two_file: Mapped[Optional[str]]
    upload_three_name: Mapped[Optional[str]]
    upload_three_file: Mapped[Optional[str]]
    # creator_id: Mapped['User'] = mapped_column(ForeignKey='users.id') # add User class

    c_main: Mapped['CounterpartiesMain'] = relationship(
        back_populates='counterparties_attribs')

