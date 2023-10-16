from sqlmodel import Session, create_engine, select

from ..models.c_parties import CounterPartiesMain, CounterpartiesAttribs
COMPANY_NAME = "CompanyX"
SQL_LOCATION = f"sqlite:///{COMPANY_NAME}.db"

def insert_cparty(engine, c_party_main: CounterPartiesMain, c_party_atribs: CounterpartiesAttribs):
    with Session(engine) as session:
        try:
            session.add(c_party_main)
            session.add(c_party_atribs)
            session.commit()
            # log here if error or return
        except Exception as e:
            return e
            #log here if error or return

def get_cparties(engine):
    with Session(engine) as session:
        statement = select(CounterPartiesMain)
        results = session.exec(statement)
        for party in results:
            print(party)

def get_cparty(engine, id:int):
    with Session(engine) as session:
        statement = select(CounterPartiesMain).join(CounterpartiesAttribs).where(CounterPartiesMain.id == id)
        result = session.exec(statement)
        print(result)