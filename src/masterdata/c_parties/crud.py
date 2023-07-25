from sqlalchemy.orm import Session
from sqlalchemy import select

from . import database

from . import model, schemas


def get_c_parties(db: Session, skip: int = 0, limit: int = 0):
    data = db.query(model.CounterpartiesMain).offset(skip).limit(limit).all()
    return data


def get_c_party(db: Session, company_id: int):
    statement = (
        select(model.CounterpartiesMain)
        .join(model.CounterpartiesMain.attributes)
        .join(model.CounterpartiesMain.additional_data)
        .where(model.CounterpartiesMain.company_id == company_id)
    )
    data = db.query(statement).first()
    return data


def create_c_party(db: Session, c_party: schemas.CounterpartiesBase):
    c_party_main = model.CounterpartiesMain(
        vatid=c_party.vatid,
        country=c_party.country, company_id=c_party.company_id,
        bank_account=c_party.bank_account, company_name_cyrilic=c_party.company_name_cyrilic,
        company_name_latin=c_party.company_name_latin, address=c_party.address
    )
    c_party_atribs = model.CounterpartiesAttribs(
        # we need to add the c_id, ORM!
        is_client=c_party.is_client, client_is_due=c_party.client_is_due,
        client_due_days=c_party.client_due_days, is_vendor=c_party.is_vendor,
        vendor_is_due=c_party.vendor_is_due, vendor_due_days=c_party.vendor_due_days,
        is_active=c_party.is_active, date_created=c_party.date_created,
        date_deactivaion=c_party.date_deactivaion)
    c_party_additional = model.CounterpartiesAdditionalData(
        # we need to add the c_id, ORM!
        main_contact_name=c_party.main_contact_name, main_contact_email=c_party.main_contact_email,
        main_contact_phone=c_party.main_contact_phone, fin_contact_name=c_party.fin_contact_name,
        fin_contact_email=c_party.fin_contact_email, fin_contact_phone=c_party.fin_contact_phone,
        upload_one_name=c_party.upload_one_name, upload_one_file=c_party.upload_one_file,
        upload_two_name=c_party.upload_two_name, upload_two_file=c_party.upload_two_file,
        upload_three_name=c_party.upload_three_name, upload_three_file=c_party.upload_three_file,
    )
    db.add_all([c_party_main, c_party_atribs, c_party_additional])
    db.commit()
