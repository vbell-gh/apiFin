from sqlmodel import Session, select
from sqlalchemy.orm.exc import NoResultFound

from src.masterdata.models.users import Users, Roles


def create_user(engine, user: Users):
    with Session(engine) as session:
        try:
            user_data = user
            session.add(user)
            session.commit()
            session.refres(user_data)
            return user_data
        except Exception as e:
            return e


def read_users(engine):
    with Session(engine) as session:
        statement = select(Users)
        results = session.exec(statement)
        return results.all()


def delete_user(engine, user_id: int):
    with Session(engine) as session:
        try:
            statement = select(Users).where(Users.id == user_id)
            results = session.exec(statement)
            user = results.one()
            session.delete(user)
            session.commit()
            return True
        except NoResultFound:
            return False


def add_role(engine, role: Roles):
    with Session(engine) as session:
        try:
            role_data = role
            session.add(role)
            session.commit()
            session.refresh(role_data)
            return role_data
        except Exception as e:
            return e


def read_roles(engine):
    with Session(engine) as session:
        statement = select(Roles)
        results = session.exec(statement)
        return results.all()
