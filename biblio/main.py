
from fastapi import FastAPI
from biblio.routers import recipe
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()


app = FastAPI()


origins = [
    "http://localhost:5173",
    "https://localhost:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(recipe)


@app.get("/")
async def root():
    return "Hello there"


@app.get("/health")
async def health():
    return {"message": "Alive and well "}
