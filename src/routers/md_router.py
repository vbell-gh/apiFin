import logging
from fastapi import APIRouter
from sqlmodel import SQLModel, create_engine


from config import ApiDefault

router = APIRouter()