
from fastapi import FastAPI
from biblio.routers import recipe
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.include_router(recipe)


@app.get("/")
async def root():
    return "Hello there"


@app.get("/health")
async def health():
    return {"message": "Alive and well "}
