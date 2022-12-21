from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from sqlalchemy import func
from biblio.sqla.models import Ingredient, Recipe
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Integer
from sqlalchemy import and_
# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
router = APIRouter(
    prefix="/search",
)


async def get_session():
    engine = create_engine(os.environ["DATABASE_URL"])
    Session = sessionmaker(bind=engine)

    return Session()


@router.get("/recipes")
async def read_items(term: str = '', session=Depends(get_session)):
    if not term:
        raise HTTPException(
            status_code=422, detail="Can't search for nothing")
    recipes = session.query(Recipe.title,
                            Recipe.link,
                            Recipe.image,
                            Recipe.cook_time,
                            Recipe.prep_time,
                            Recipe.rest_time, func.array_agg(Ingredient.name, type_=ARRAY(Integer)).label('ingredients')).select_from(Recipe, Ingredient).filter(
        Recipe.title.contains(term)).join(Ingredient).group_by(Recipe)
    return [recipe for recipe in recipes]


@ router.get("/ingredients/")
async def read_items(terms: str = '', session=Depends(get_session)):
    if not terms:
        raise HTTPException(
            status_code=422, detail="Can't search for nothing")
    ingredients = terms.split(',')

    filters = []

    for ingredient in ingredients:
        subquery = session.query(Ingredient.recipe_id).filter(
            Ingredient.name.contains(ingredient))
        filters.append(Recipe.id.in_(subquery))

    recipes = (session.query(Recipe.title,
                             Recipe.link,
                             Recipe.image,
                             Recipe.cook_time,
                             Recipe.prep_time,
                             Recipe.rest_time,
                             func.array_agg(Ingredient.name, type_=ARRAY(Integer)).label('ingredients'))
               .select_from(Recipe, Ingredient)
               .filter(and_(*filters))
               .join(Ingredient)
               .group_by(Recipe))

    return recipes.all()
