from fastapi import FastAPI, Depends, HTTPException
from src.masterdata.router import router

app = FastAPI()
app.include_router(router)
