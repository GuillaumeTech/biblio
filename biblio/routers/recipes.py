from fastapi import APIRouter, Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from biblio.sqla.models import Recipe


router = APIRouter(
    prefix="/recipes",
)


async def get_session():
    engine = create_engine(os.environ["DATABASE_URL"])
    Session = sessionmaker(bind=engine)

    return Session()


@router.get("/search/{text}")
async def read_items(text: str, session=Depends(get_session)):
    recipes = session.query(Recipe).filter(Recipe.title.contains(text))
    return [recipe for recipe in recipes]
