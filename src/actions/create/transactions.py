import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import transactions as models_tr
from src.schemas import transactions as schemas_tr
from src.actions.background.ar_transactions import ARTransactionsPosting


def process_ar_document(db: Session, document: schemas_tr.ARTransactions):
    doc = ARTransactionsPosting(db, document)
    result = doc.main()
    return result
