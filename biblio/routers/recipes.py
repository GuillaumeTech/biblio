from fastapi import APIRouter, Depends, HTTPException
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


@router.get("/search/")
async def read_items(term: str = '', session=Depends(get_session)):
    if not term:
        raise HTTPException(
            status_code=422, detail="Can't search for nothing")
    recipes = session.query(Recipe).filter(Recipe.title.contains(term))
    return [recipe for recipe in recipes]
