from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from masterdata.models import c_parties
from masterdata.schemas import c_parties


from masterdata.crud import c_parties
from masterdata.database import SessionLocal, engine

c_parties.Base.metadata.create_all(bind=engine)

app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try: 
#         yield db
#     finally:
#         db.close()
        
# @app.post("/counterparties/", response_model=schemas.CounterpartiesBase)
# def create_counterpary(c_party: schemas.CounterpartiesBase, db: Session = Depends(get_db)):
#     c_pary_data = crud.create_c_party(db, c_party)
#     if c_pary_data:
#         raise HTTPException(status_code=400, detail)
#     return crud.create_c_party(db, c_party=)
