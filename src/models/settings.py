from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base declarative class for all models."""

    __abstract__ = True


class DocumentTypes(Base):
    __tablename__ = "document_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    desctiption: Mapped[Optional[str]]


class Logs(Base):  # idea for now python loggin module is enough
    __tablename__ = "logs"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created: Mapped[datetime]
    operation_id: Mapped[int] = mapped_column(ForeignKey("gl_transactions.id"))


class AppSettings(Base): # for now can be a simple json file
    __tablename__ = "app_settings"
    id: Mapped[int] = mapped_column(primary_key=True)
    abbreviation: Mapped[str]
    name: Mapped[str]
    value: Mapped[str]
    description: Mapped[Optional[str]]

# Add currency table

