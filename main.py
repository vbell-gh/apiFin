from fastapi import FastAPI
from sqlalchemy import create_engine
import uvicorn
from src.models.master_data import Base as Base_md
from src.models.transactions import Base as Base_tr
from src.models.settings import Base as Base_set
from src.routers.md_router import md_router
from config import ApiDefault


settings = ApiDefault()
DB_LOCATION = settings.db_location

print(DB_LOCATION)
engine = create_engine(DB_LOCATION, echo=True)


def create_db_if_not_exists():
    """create_db_if_not_exists Creates the database tables defined in the models
    """
    Base_md.metadata.create_all(engine)
    Base_tr.metadata.create_all(engine)
    Base_set.metadata.create_all(engine)


app = FastAPI(lifespan=create_db_if_not_exists())
app.include_router(md_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)