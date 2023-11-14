import logging
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import master_data as models_md
from src.schemas import master_data as schemas_md


def create_vendor(db: Session, vendor: schemas_md.VendorDetails):
    try:
        db_vendor = models_md.VendorsMasterData(
            vatid=vendor.vatid,
            country=vendor.country,
            company_id=vendor.company_id,
            bank_account=vendor.bank_account,
            company_name_cyrilic=vendor.company_name_cyrilic,
            company_name_latin=vendor.company_name_latin,
            address=vendor.address,
        )
        db.add(db_vendor)
        db.commit()
        db.refresh(db_vendor)
        db_vendor_attribs = models_md.VendorMDAtribs(
            c_id=db_vendor.id,
            vendor_is_due=vendor.vendor_is_due,
            vendor_due_days=vendor.due_days,
            is_active=vendor.is_active,
            main_contact_name=vendor.main_contact_name,
            main_contact_email=vendor.main_contact_email,
            main_contact_phone=vendor.main_contact_phone,
            fin_contact_name=vendor.fin_contact_name,
            fin_contact_email=vendor.fin_contact_email,
            fin_contact_phone=vendor.fin_contact_phone,
            upload_one_name=vendor.upload_one_name,
            upload_one_file=vendor.upload_one_file,  # file path
            upload_two_name=vendor.upload_two_name,
            upload_two_file=vendor.upload_two_file,
            upload_three_name=vendor.upload_three_name,
            upload_three_file=vendor.upload_three_file,
        )
        db.add(db_vendor_attribs)
        db.commit()
        logging.info("Vendor created successfully")
    except SQLAlchemyError as e:
        logging.error("Error creating vendor: %s", e)
        raise e


def create_client(db: Session, client: schemas_md.ClientDetails):
    try:
        db_client = models_md.ClientsMasterData(
            vatid=client.vatid,
            country=client.country,
            company_id=client.company_id,
            bank_account=client.bank_account,
            company_name_cyrilic=client.company_name_cyrilic,
            company_name_latin=client.company_name_latin,
            address=client.address,
        )
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        db_client_attribs = models_md.ClientsMDAtribs(
            c_id=db_client.id,
            client_is_due=client.client_is_due,
            client_due_days=client.due_days,
            is_active=client.is_active,
            main_contact_name=client.main_contact_name,
            main_contact_email=client.main_contact_email,
            main_contact_phone=client.main_contact_phone,
            fin_contact_name=client.fin_contact_name,
            fin_contact_email=client.fin_contact_email,
            fin_contact_phone=client.fin_contact_phone,
            upload_one_name=client.upload_one_name,
            upload_one_file=client.upload_one_file,
            upload_two_name=client.upload_two_name,
            upload_two_file=client.upload_two_file,
            upload_three_name=client.upload_three_name,
            upload_three_file=client.upload_three_file,
        )
        db.add(db_client_attribs)
        db.commit()
        logging.info("Client created successfully")
    except SQLAlchemyError as e:
        logging.error("Error creating client: %s", e)
        raise e


def create_gl_account(db: Session, gl_account: schemas_md.GLAccountsMDBase):
    try:
        db_gl_account = models_md.GLAccountsMD(
            code=gl_account.code,
            name=gl_account.name,
            type=gl_account.type,
            category=gl_account.category,
            subcategory=gl_account.subcategory,
            description=gl_account.description,
            is_active=True,
        )
        db.add(db_gl_account)
        db.commit()
        logging.info("GL Account created successfully, no: %s", db_gl_account.id)
    except SQLAlchemyError as e:
        logging.error("Error creating GL Account: %s", e)
        raise e


def create_material(db: Session, material=schemas_md.InventoryMD):
    try:
        vendord_id = (
            db.query(models_md.VendorsMasterData)
            .filter(
                models_md.VendorsMasterData.company_name_latin == material.vendor_name
            )
            .first()
            .id
        )
        db_material = models_md.InvenotriesMD(
            material_code=material.material_code,
            name=material.name,
            description=material.description,
            category=material.category,
            sub_category=material.sub_category,
            unit_of_measure=material.unit_of_measure,
            barcode=material.barcode,
            is_active=material.is_active,
            vendor_code=vendord_id,
            date_created=datetime.now(),
        )
        db.add(db_material)
        db.commit()
        db.refresh(db_material)
        db_material_attribs = models_md.InvenotriesAtributes(
            i_id=db_material.id,
            custom_code=material.customs_code,
            customs_description=material.customs_description,
            main_unit=material.main_unit,
            net_weight=material.net_weight,
            gross_weight=material.gross_weight,
            height=material.height,
            width=material.width,
            storage_location=material.storage_location,
            photo_1_location=material.photo_1_location,
            photo_2_location=material.photo_2_location,
            photo_3_location=material.photo_3_location,
            photo_4_location=material.photo_4_location,
        )
        db.add(db_material_attribs)
        db.commit()
        logging.info(
            "Material created successfully, no: %s, name: %s",
            db_material.material_code,
            db_material.name,
        )
    except SQLAlchemyError as e:
        logging.error("Error creating Material: %s", e)
        raise e


def create_service(db: Session, service=schemas_md.ServicesMD):
    try:
        db_service = models_md.ServicesMD(
            name=service.name,
            description=service.description,
            category=service.category,
            sub_category=service.sub_category,
            account=service.account,
        )
        db.add(db_service)
        db.commit()
        logging.info("Service created successfully, name: %s", db_service.name)
    except SQLAlchemyError as e:
        logging.error("Error creating Service: %s", e)
        raise e


def create_user(db: Session, user: schemas_md.UserCreate):
    try:
        db_user = models_md.User(
            username=user.username,
            password=user.password,
            fullname=user.fullname,
            email=user.email,
            role_id=user.role_id,
        )
        db.add(db_user)
        db.commit()
        logging.info("User created successfully, no: %s", db_user.username)
    except SQLAlchemyError as e:
        logging.error("Error creating User: %s", e)
        raise e


def create_role(db: Session, role: schemas_md.Role):
    try:
        db_role = models_md.Role(
            role_name=role.role_name,
            description=role.description,
        )
        db.add(db_role)
        db.commit()
        logging.info("Role created successfully, no: %s", db_role.role_name)
    except SQLAlchemyError as e:
        logging.error("Error creating Role: %s", e)
        raise e
