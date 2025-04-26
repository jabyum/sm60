from fastapi import FastAPI
app = FastAPI(docs_url="/")
from api.photo_api.photo import photo_api
from database import Base, engine
from database.models import *
app.include_router(photo_api)
# uvicorn main:app --reload
Base.metadata.create_all(bind=engine)
