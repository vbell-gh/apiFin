from contextlib import asynccontextmanager
from fastapi import APIRouter, Depends, HTTPException


from src.schemas import transactions as schemas_tr

@asynccontextmanager
async def create_trasnactions_tables(app: APIRouter):
    


router = APIRouter(prefix="/transaction")


@router.post("/AR")
def post_ar_transaction(document: schemas_tr.ARTransactions):
    pass
