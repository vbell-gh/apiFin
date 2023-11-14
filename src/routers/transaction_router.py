from fastapi import APIRouter
from sqlalchemy import create_engine

from src.actions.create import master_data as create_md
from src.schemas import transactions as schemas_tr
from config import ApiDefault

settings = ApiDefault()
DB_LOCATION = settings.db_location

engine = create_engine(DB_LOCATION, echo=True)

tr_router = APIRouter(prefix="/transaction")


