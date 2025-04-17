from fastapi import FastAPI
app = FastAPI(docs_url="/")
from api.photo_api.photo import photo_api
app.include_router(photo_api)
# uvicorn main:app --reload