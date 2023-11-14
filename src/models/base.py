from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base declarative class for all models."""

    __abstract__ = True

