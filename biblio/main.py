from fastapi import Depends, FastAPI

from routers import recipe

app = FastAPI()


app.include_router(recipe)


@app.get("/")
async def root():
    return "Hello there"


@app.get("/health")
async def health():
    return {"message": "Alive and well "}