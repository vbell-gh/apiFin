import logging
from sqlmodel import Session, select, update
from sqlalchemy.exc import SQLAlchemyError

from src.masterdata.models.gl import GLAccounts


def create_account(engine, account: GLAccounts):
    with Session(engine) as session:
        try:
            session.add(account)
            session.commit()
            session.refresh(account)
            return account
        except SQLAlchemyError as e:
            logging.error(e)
            raise e


def get_accounts(engine):
    try:
        with Session(engine) as session:
            statement = select(GLAccounts)
            results = session.exec(statement)
            return results.fetchall()
    except SQLAlchemyError as e:
        logging.error(e)
        return e


def delete_account(engine, account_id: int):
    with Session(engine) as session:
        try:
            statement = select(GLAccounts).where(GLAccounts.id == account_id)
            result = session.exec(statement).first()
            session.delete(result)
            session.commit()
            return result
        except SQLAlchemyError as e:
            logging.error(e)
            raise e

def update_account(engine, account: GLAccounts):
    with Session(engine) as session:
        # There should be an if statement to check if the account has posting transactions
        # if it does only nameing can be changed
        try:
            statement = update(GLAccounts).where(GLAccounts.id == account.id).values(
                account_code=account.account_code,
                account_name=account.account_name,
                account_type=account.account_type,
                account_category=account.account_category,
                account_subcategory=account.account_subcategory,
                account_description=account.account_description,
                account_status=account.account_status,
                account_created=account.account_created,
                account_creator=account.account_creator
            )
            session.exec(statement)
            session.commit()
            return account
        except SQLAlchemyError as e:
            logging.error(e)
            raise e
