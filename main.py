from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.masterdata.models.c_parties import Base
import os
# from masterdata.schemas.c_parties import c_parties

from config import Settings

settings = Settings()

from src.masterdata.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
