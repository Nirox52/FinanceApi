from fastapi import FastAPI
from database import Base, engine
from models import  operations, users
from routers import user_router, operation_router

app = FastAPI()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(operation_router.router)

@app.get("/")
def root():
    return {"message": "Finance App"}

