import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import master_data as models_tr
from src.models import settings as models_setings
from src.schemas import master_data as schemas_tr


def get_client_id(db: Session, name: str):
    try:
        client = (
            db.query(models_tr.ClientsMasterData)
            .filter(models_tr.ClientsMasterData.company_name_latin == name)
            .first()
        )
        return client.id
    except SQLAlchemyError as e:
        logging.error(e)
        raise e


def get_vendor_id(db: Session, name: str):
    try:
        vendor = (
            db.query(models_tr.VendorsMasterData)
            .filter(models_tr.VendorsMasterData.company_name_latin == name)
            .first()
        )
        return vendor.id
    except SQLAlchemyError as e:
        logging.error(e)
        raise e


def get_cparty_duedays(db: Session, client_id=None, vendor_id=None) -> int:
    """get_cparty_duedays returns the days due for a given client or vendor

    Args:
        db (Session): DB Session
        client_id (int, optional): Client ID. Defaults to None.
        vendor_id (int, optional): Vendor ID. Defaults to None.

    Raises:
        e: when there is an error in DB access

    Returns:
        int: Days due
    """
    try:
        if client_id:
            client = (
                db.query(models_tr.ClientsMasterData)
                .filter(models_tr.ClientsMasterData.id == client_id)
                .first()
            )
            return client.days_due
        elif vendor_id:
            vendor = (
                db.query(models_tr.VendorsMasterData)
                .filter(models_tr.VendorsMasterData.id == vendor_id)
                .first()
            )
            return vendor.days_due
        else:
            raise Exception("No client or vendor ID provided")
    except SQLAlchemyError as e:
        logging.error(e)
        raise e
