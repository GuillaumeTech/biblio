from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from sqlalchemy import func
from biblio.sqla.models import Ingredient, Recipe
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Integer
from sqlalchemy import or_
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
    recipe_id_query = session.query(
        Ingredient.recipe_id, func.array_agg(Ingredient.name, type_=ARRAY(Integer)).label('ingredients'), func.count(Ingredient.recipe_id).label('count')).group_by(Ingredient.recipe_id)
    ingredients_filters = []

    for ingredient in ingredients:
        ingredients_filters.append(
            Ingredient.name.contains(ingredient))

    recipe_id_query = recipe_id_query.filter(or_(*ingredients_filters))
    recipe_id_query = recipe_id_query.having(
        func.count(Ingredient.recipe_id) == len(ingredients))

    result = recipe_id_query.all()
    print(result)

    return result
#  CREATE TABLE test (   id INT,
#   ingredients VARCHAR[] );
# INSERT INTO test (id, ingredients) VALUES (1, '{"bla", "blo","bli"}');
# INSERT INTO test (id, ingredients) VALUES (2, '{"bla", "blo","bli"}');


# SELECT id FROM (SELECT id, unnest(ingredients) as HUM FROM test) as unnested Where HUM LIKE '%lo%' OR HUM LIKE '%la%' GROUP BY unnested.id
