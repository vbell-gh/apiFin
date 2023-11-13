import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import transactions as models_tr
from src.schemas import transactions as schemas_tr
from src.models import settings as app_settings


class ARTransactionsPosting:
    """This class is used to post AR Transactions the actions posting in all tables based on the documet type are defined here."""

    def __init__(self, db: Session, document: schemas_tr.ARTransactions) -> None:
        self.db = db
        self.document = document  # the pydantic instance of the posting document
        self.doc_type = document.documment_type  # the type of the posting document
        self.next_doc_no = self.get_next_doc_no()  # the next document number
        self.doc_model = (
            None  # here is stored the document insrance throughout processing
        )
        self.gl_document = []  # here are stored the GL entries prior to posting

        self.ar_account = 9999  # this is the receivables account should be changed
        self.tax_account = 9998  # this is the tax account should be changed

    def get_next_doc_no(self) -> int:
        """get_next_doc_no Returns the next document number for a given document type

        Raises:
            e: when there is DB Access issue

        Returns:
            int: The doc number to be used
        """
        try:
            doc_types = (
                self.db.query(app_settings.DocumentTypes)
                .filter(app_settings.DocumentTypes.doc_abbreviation == self.doc_type)
                .first()
            )
            doc_no = doc_types.counter
            return doc_no
        except SQLAlchemyError as e:
            logging.error(e)
            raise e

    def increment_next_doc_no(self) -> None:
        """increment_next_doc_no use this when a document is posted
        Raises:
            e: when there is an error in DB access
        """
        try:
            self.db.query(app_settings.DocumentTypes).filter(
                app_settings.DocumentTypes.doc_abbreviation == self.doc_type
            ).update(
                {
                    app_settings.DocumentTypes.counter: app_settings.DocumentTypes.counter
                    + 1
                }
            )
            self.db.commit()
            logging.info("Document number incremented")
        except SQLAlchemyError as e:
            logging.error(e)
            raise e

    def process_line_ites(self) -> None:
        """process_line_ites Parses the line items recieved based on the document type
        if the lines are based on Service or Goods MD then the lines are parsed and added to the document instance
        If the documents are not based, the accounts are passed in the GL directly
        """
        if self.doc_type == "SSR":  # SSR = Service sales rows
            for line in self.document.document_lines:
                self.doc_model.services_sales_lines.append(
                    document_id=self.doc_model.id,
                    material_id=line.line_item_id,
                    account_id=line.account_id,
                    custom_line_name=line.custom_line_name,
                    unit_price=line.unit_price,
                    quantity=line.quantity,
                    amount=line.quantity * line.unit_price,
                )
        elif self.doc_type == "GSR":  # GSR = Good sales rows
            for line in self.document.document_lines:
                self.doc_model.goods_sales_lines.append(
                    document_id=self.doc_model.id,
                    material_id=line.line_item_id,
                    account_id=line.account_id,
                    custom_line_name=line.custom_line_name,
                    unit_price=line.unit_price,
                    quantity=line.quantity,
                    amount=line.quantity * line.unit_price,
                )
        else:
            self.document.document_lines = None

            # create the document association
            doc_association = models_tr.DocumentsAssociation()
            doc_association.document_type = self.doc_model.document_type
            self.db.add(doc_association)
            self.db.commit()
            self.doc_model.documents_association_id = doc_association.id
            self.db.add(self.doc_model)
            self.db.commit()

    def generate_gl_entries(self) -> None:
        """generate_gl_entries this method generates the GL entries for the document,
        based on which are posted with the DocumentASsociation model

        Raises:
            ValueError: Document type not implemented
            ValueError: Document type not supported
        """
        if self.doc_type == "SSR":
            # revenue CR items
            for line in self.document.document_lines:
                self.gl_document.append(
                    type_of_operation="CR",
                    account_no=line.account_id,
                    amount=line.amount,
                    line_text=line.custom_line_name,
                    created=datetime.now(),
                )
            # DR receivables
            self.gl_document.append(
                type_of_operation="DR",
                account_no=self.ar_account,
                amount=self.document.gross_amount,
                line_text=f"AR {self.document.counter_party_name}",
                created=datetime.now(),
            )
            # CR tax amount
            self.gl_document.append(
                type_of_operation="CR",
                account_no=self.tax_account,
                amount=self.document.tax_amount,
                line_text=f"Tax {self.document.tax_code}",
                created=datetime.now(),
            )
        elif self.doc_type == "GSR":
            raise ValueError("Document type not supported yet")
            # This needs to be implemented later as COGS need to be processed also
        elif self.doc_type == "SOME_OTHER DOCUMENT":
            raise ValueError("Document type not supported yet")
            # This needs to be implemented later when it is decided what the types of documents will be
        else:
            raise ValueError("Document type not supported")

    def main(self):
        try:
            document = self.document  # define a local variable for document
            # Create the AR document model instance
            self.doc_model = models_tr.ARTransactions(
                so_id=document.so_id,
                document_type=document.documment_type,
                internal_doc_ref=self.next_doc_no,
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
            if self.doc_type == "SSR" or self.doc_type == "GSR":
                self.process_line_ites()
            # create the document lines in the AR document instance
            self.gl_document = models_tr.DocumentsAssociation(
                document_type=self.doc_model.document_type,
                doc_sub_type=None,
            )
            self.generate_gl_entries()
            return True
        except SQLAlchemyError as e:
            logging.error(e)
            raise e
