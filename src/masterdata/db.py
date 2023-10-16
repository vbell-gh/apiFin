from sqlmodel import SQLModel, create_engine

from config import ApiDefault
from src.masterdata.models.c_parties import CounterPartiesMain, CounterpartiesAttribs

def engine(ApiDefault):
    SQLITE_LOCATION = f"sqlite://./{ApiDefault.database_location}/{ApiDefault.company_name}.db"
    engine = create_engine(SQLITE_LOCATION, echo=True)
    return engine

def create_tables(engine):
    SQLModel.metadata.create_all(engine)