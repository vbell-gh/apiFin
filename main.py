from fastapi import FastAPI, Depends, HTTPException
from src.masterdata.router import router
import uvicorn
from src.masterdata.models.c_parties import CounterpartiesAttribs, CounterPartiesMain

app = FastAPI()
app.include_router(router)
