import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import transactions as models_tr
from src.schemas import transactions as schemas_tr
from src.actions.background import transactions as actions_tr


def post_service_sales_document(db: Session, document: schemas_tr.ARTransactions):
    try:
        ar_doc = models_tr.ARTransactions(
            so_id=document.so_id,
            internal_doc_ref=actions_tr.get_next_doc_no(
                db, document.documment_type
            ),  # get next doc no
            document_date=document.documnent_date,
            date_posted=datetime.now(),  # get current date
            days_due=document.due_days,  # vendor due days need to be fetched from master data prior to posting
            c_id=document.counter_party_name,  # find  cparty id based on name
            tax_code=document.tax_code,
            net_amount=document.net_amount,
            gross_amount=document.gross_amount,
            tax_amount=document.tax_amount,
            currency=document.currency,
            services_sales_lines=document.document_lines,
        )
        doc_association = models_tr.DocumentsAssociation()
        doc_association.document_type = ar_doc.document_type
        db.add(doc_association)
        db.commit()
        ar_doc.documents_association_id = doc_association.id
        db.add(ar_doc)
        db.commit()
        return ar_doc
    except SQLAlchemyError as e:
        logging.error(e)
        raise e


def post_goods_sales_document(db: Session, document: schemas_tr.ARTransactions):
    try:
        ar_doc = models_tr.ARTransactions(
            so_id=document.so_id,
            internal_doc_ref=actions_tr.get_next_doc_no(
                db, document.documment_type
            ),  # get next doc no
            document_date=document.documnent_date,
            date_posted=datetime.now(),  # get current date
            days_due=document.due_days,  # vendor due days need to be fetched from master data prior to posting
            c_id=document.counter_party_name,  # find  cparty id based on name
            tax_code=document.tax_code,
            net_amount=document.net_amount,
            gross_amount=document.gross_amount,
            tax_amount=document.tax_amount,
            currency=document.currency,
            goods_sales_lines=document.document_lines,
        )
        doc_association = models_tr.DocumentsAssociation()
        doc_association.document_type = ar_doc.document_type
        db.add(doc_association)
        db.commit()
        ar_doc.documents_association_id = doc_association.id
        db.add(ar_doc)
        db.commit()
        return ar_doc
    except SQLAlchemyError as e:
        logging.error(e)
        raise e


def post_general_ar_document(db: Session, document: schemas_tr.ARTransactions):
    try:
        ar_doc = models_tr.ARTransactions(
            so_id=document.so_id,
            internal_doc_ref=actions_tr.get_next_doc_no(
                db, document.documment_type
            ),  # get next doc no
            document_date=document.documnent_date,
            date_posted=datetime.now(),  # get current date
            days_due=document.due_days,  # vendor due days need to be fetched from master data prior to posting
            c_id=document.counter_party_name,  # find  cparty id based on name
            tax_code=document.tax_code,
            net_amount=document.net_amount,
            gross_amount=document.gross_amount,
            tax_amount=document.tax_amount,
            currency=document.currency,
        )
        doc_association = models_tr.DocumentsAssociation()
        doc_association.document_type = ar_doc.document_type
        db.add(doc_association)
        db.commit()
        ar_doc.documents_association_id = doc_association.id
        db.add(ar_doc)
        db.commit()
        return ar_doc
    except SQLAlchemyError as e:
        logging.error(e)
        raise e
