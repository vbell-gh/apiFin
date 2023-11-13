from fastapi import FastAPI
from src.routers import md_router, transaction_router
import uvicorn

app = FastAPI()
app.include_router(md_router.router)
app.include_router(transaction_router.router)

@app.on_event("startup")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
