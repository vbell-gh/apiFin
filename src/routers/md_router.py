from fastapi import APIRouter
from sqlalchemy import create_engine

from config import ApiDefault

from src.actions.create import master_data as create_md
from src.schemas import master_data as schemas_md

settings = ApiDefault()
DB_LOCATION = settings.db_location
engine = create_engine(DB_LOCATION, echo=True)

md_router = APIRouter(prefix="/master_data")


@md_router.post("/create_vendor")
def create_vendor(vendor: schemas_md.VendorDetails):
    create_md.create_vendor(engine, vendor)


@md_router.post("/create_client")
def create_client(client: schemas_md.ClientDetails):
    create_md.create_client(engine, client)


@md_router.post("/create_gl_account")
def create_gl_account(gl_account: schemas_md.GLAccountsMDBase):
    create_md.create_gl_account(engine, gl_account)


@md_router.post("/create_material")
def create_material(material: schemas_md.InventoryMD):
    create_md.create_material(engine, material)


@md_router.post("/create_service")
def create_service(service: schemas_md.ServicesMD):
    create_md.create_service(engine, service)


@md_router.post("/create_user")
def create_user(user: schemas_md.UserCreate):
    create_md.create_user(engine, user)


@md_router.post("/create_role")
def create_role(role: schemas_md.RoleBase):
    create_md.create_role(engine, role)
