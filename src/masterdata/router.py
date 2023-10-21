import logging
from fastapi import APIRouter
from sqlmodel import SQLModel, create_engine

from src.masterdata.crud.c_parties import insert_cparty, get_cparties, get_cparty
# , add_role, read_roles
from src.masterdata.crud.users import create_user, read_users, delete_user
from src.masterdata.crud.gl import create_account, get_accounts, delete_account, update_account

from src.masterdata.models.gl import GLAccounts
from src.masterdata.models.c_parties import CounterPartiesMain, CounterpartiesAttribs
from src.masterdata.models.users import Users  # , Roles

from src.masterdata.dummy_data.generate import generate_dummies

from config import ApiDefault

router = APIRouter()

SQLITE_LOCATION = f"sqlite:///{ApiDefault().database_location}/{ApiDefault().company_name}.db"
engine = create_engine(SQLITE_LOCATION, echo=True)


@router.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)

    # creates dumy data if development mode is on and db is empty
    if ApiDefault().development:
        logging.info("Dev mode is on")
        result = get_cparties(engine)
        if len(result) < 1:
            logging.info("No data found generating dummy data")
            generate_dummies(engine)


@router.post("/c_party/")
def create_cparty(main: CounterPartiesMain, atribs: CounterpartiesAttribs):
    c_party = insert_cparty(engine, c_party_main=main, c_party_atribs=atribs)
    return c_party


@router.get("/c_parties/")
def read_cparties():
    parties = get_cparties(engine)
    return parties


@router.get("/c_party/")
def read_cparty(c_party_id: int):
    party = get_cparty(engine, c_party_id)
    return party


@router.post("/user/")
def add_user(user: Users):
    user = create_user(engine, user)
    return user


@router.get("/users/")
def get_users():
    users = read_users(engine)
    return users


@router.delete("/user/")
def remove_user(user_id: int):
    user = delete_user(engine, user_id)
    return user


@router.post("/gl_account/")
def add_account(account: GLAccounts):
    account = create_account(engine, account)
    return account


@router.get("/gl_accounts/")
def read_accounts():
    accounts = get_accounts(engine)
    return accounts


@router.delete("/gl_account/")
def remove_account(account_id: int):
    account = delete_account(engine, account_id)
    return account


@router.put("/gl_account/")
def change_account(account: GLAccounts):
    account = update_account(engine, account)
    return account
