import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import transactions as models_tr
from src.schemas import transactions as schemas_tr




def check_posting_balancing(cr_postings: list, dr_posting: list):
    dr_sum = sum(cr_postings)
    cr_sum = sum(dr_posting)
    if dr_sum != cr_sum:
        raise ValueError(
            f"Posting not balanced. DR: {dr_sum} CR: {cr_sum} Difference: {dr_sum - cr_sum}"
        )
    else:
        return True
