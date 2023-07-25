from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
company_name = "CompanyX"

db_folder = os.path.join(current_dir, "..", ".." ,".." ,"database")

SQL_DB_URL = f"sqlite:///{db_folder}/{company_name}.db"
engine = create_engine(
    SQL_DB_URL, 
    connect_args={'check_same_thread':False}, # the cocnect_args are only for sqlite
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


