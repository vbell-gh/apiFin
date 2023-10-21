from src.masterdata.crud.c_parties import insert_cparty
from src.masterdata.crud.users import create_user, add_role
from src.masterdata.crud.gl import create_account

from src.masterdata.dummy_data.data.c_parties import c_parties_main_dummies, c_parties_attribs_dummies
from src.masterdata.dummy_data.data.users import users_dummy_data, roles_dummy_data
from src.masterdata.dummy_data.data.gl import accounts_dummy


def generate_dummies(engine):
    for main, attribs in zip(c_parties_main_dummies, c_parties_attribs_dummies):
        insert_cparty(engine=engine, c_party_main=main, c_party_atribs=attribs)

    for user in users_dummy_data:
        create_user(engine=engine, user=user)

    for role in roles_dummy_data:
        add_role(engine=engine, role=role)

    for account in accounts_dummy:
        create_account(engine=engine, account=account)
