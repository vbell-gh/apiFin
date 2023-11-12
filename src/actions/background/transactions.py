import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import transactions as models_tr
from src.schemas import transactions as schemas_tr
from src.models import settings as app_settings


def get_next_doc_no(db: Session, doc_abbreviation: str) -> int:
    """get_next_doc_no Returns the next document number for a given document type

    Args:
        db (Session): DB Session
        doc_abbreviation (str): Abbreviation of the document type

    Raises:
        e: when there is DB Access issue

    Returns:
        int: The doc number to be used
    """
    try:
        doc_types = (
            db.query(app_settings.DocumentTypes)
            .filter(app_settings.DocumentTypes.doc_abbreviation == doc_abbreviation)
            .first()
        )
        doc_no = doc_types.counter
        return doc_no
    except SQLAlchemyError as e:
        logging.error(e)
        raise e


def increment_next_doc_no(db: Session, doc_abbreviation: str) -> None:
    """increment_next_doc_no use this when a document is posted

    Args:
        db (Session): DB Session
        doc_abbreviation (str): Abbreviation of the document type

    Raises:
        e: when there is an error in DB access
    """
    try:
        doc_types = (
            db.query(app_settings.DocumentTypes)
            .filter(app_settings.DocumentTypes.doc_abbreviation == doc_abbreviation)
            .first()
        )
        doc_types.counter += 1
        db.commit()
    except SQLAlchemyError as e:
        logging.error(e)
        raise e

