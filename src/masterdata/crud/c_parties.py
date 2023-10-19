from sqlmodel import Session, select

from src.masterdata.models.c_parties import CounterPartiesMain, CounterpartiesAttribs


def insert_cparty(engine, c_party_main: CounterPartiesMain, c_party_atribs: CounterpartiesAttribs):
    with Session(engine) as session:
        try:

            main_cparty = c_party_main
            session.add(main_cparty)
            session.commit()
            session.refresh(main_cparty)
            atribs_cparty = c_party_atribs
            atribs_cparty.c_id = main_cparty.id
            session.add(atribs_cparty)
            session.commit()
            session.refresh(atribs_cparty)
            return c_party_main
            # log here if error or return
        except Exception as e:
            print(e)
            return e
            # log here if error or return


def get_cparties(engine):
    with Session(engine) as session:
        statement = select(CounterPartiesMain)
        results = session.exec(statement)
        return list(results
                    )


def get_cparty(engine, id: int):
    with Session(engine) as session:
        statement = select(CounterPartiesMain, CounterpartiesAttribs).where(
            CounterPartiesMain.id == id)
        statement = statement.join(
            CounterpartiesAttribs, CounterPartiesMain.id == CounterpartiesAttribs.c_id)
        result = session.exec(statement).first()
        return result
