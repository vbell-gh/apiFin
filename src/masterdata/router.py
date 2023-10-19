from fastapi import APIRouter
from sqlmodel import SQLModel, create_engine

from src.masterdata.crud.c_parties import insert_cparty, get_cparties, get_cparty
from src.masterdata.crud.users import create_user, read_users, delete_user, add_role, read_roles
from src.masterdata.models.c_parties import CounterPartiesMain, CounterpartiesAttribs
from src.masterdata.models.users import User, Roles

from config import ApiDefault

router = APIRouter()

SQLITE_LOCATION = f"sqlite:///{ApiDefault().database_location}/{ApiDefault().company_name}.db"
engine = create_engine(SQLITE_LOCATION, echo=True)


@router.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)


@router.post("/c_party/")
def create_cparty(main: CounterPartiesMain, atribs: CounterpartiesAttribs):
    c_party = insert_cparty(engine, c_party_main=main, c_party_atribs=atribs)
    return c_party


@router.get("/c_parties/")
def read_cparties():
    parties = get_cparties(engine)
    return parties


@router.get("/c_party/")
def read_cparty(id: int):
    party = get_cparty(engine, id)
    return party


@router.post("user/")
def add_user(user: User):
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
