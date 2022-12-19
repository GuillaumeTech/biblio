
import pandas as pd
from sqlalchemy import create_engine
import os
import sys
from dotenv import load_dotenv
from tqdm import tqdm


def chunker(seq, size):
    # from http://stackoverflow.com/a/434328
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def insert_with_progress(df, db, table_name):
    chunksize = int(len(df) / 10)  # 10%
    with tqdm(total=len(df)) as pbar:
        for i, cdf in enumerate(chunker(df, chunksize)):
            cdf.to_sql(table_name, db, if_exists='append', index=False)
            pbar.update(chunksize)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

data_dir = f"{BASE_DIR}/scripts/data"

ricardo = pd.read_json(f'{data_dir}/ricardo.json', encoding="utf8")
marmitton = pd.read_json(f'{data_dir}/marmiton.json', encoding="utf8")
septcinq = pd.read_json(f'{data_dir}/750g.json', encoding="utf8")
cuisine_az = pd.read_json(f'{data_dir}/cuisine_az.json', encoding="utf8")
marieclaire = pd.read_json(f'{data_dir}/marieclaire.json', encoding="utf8")

frames = [ricardo, marmitton, septcinq, cuisine_az, marieclaire]

result = pd.concat(frames)
result.insert(0, 'id', range(0, len(result)))
result = result.explode('ingredients')

ingredients = result.iloc[:, [0, 4]]
ingredients = ingredients.rename(
    columns={"id": 'recipe_id', 'ingredients': 'name'})


recipes = result.iloc[:, [0, 1, 2, 3, 5, 6, 7]]
recipes = recipes.drop_duplicates()

db = create_engine(os.environ["DATABASE_URL"])

print("inserting recipes")
insert_with_progress(recipes, db, 'recipe')
print("inserting ingredients")
insert_with_progress(ingredients, db, 'ingredient')
