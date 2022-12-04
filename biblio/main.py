from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from routers import recipe

app = FastAPI()


app.include_router(recipe.router)


@app.get("/")
async def root():
    return "Hello there"


@app.get("/health")
async def health():
    return {"message": "Alive and well "}