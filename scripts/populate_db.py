
import pandas as pd
from sqlalchemy import create_engine
import os, sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

data_dir = f"{BASE_DIR}/scripts/data"

ricardo = pd.read_json(f'{data_dir}/ricardo.json', encoding="utf8")
marmitton = pd.read_json(f'{data_dir}/marmiton.json', encoding="utf8")
septcinq = pd.read_json(f'{data_dir}/750g.json', encoding="utf8")
cuisine_az = pd.read_json(f'{data_dir}/cuisine_az.json', encoding="utf8")
marieclaire = pd.read_json(f'{data_dir}/marieclaire.json', encoding="utf8")

db = create_engine(os.environ["DATABASE_URL"])

ricardo.to_sql('recipe', db, if_exists='replace', index = False)
print("inserted ricardo data")

marmitton.to_sql('recipe', db, if_exists='replace', index = False)
print("inserted marmitton data")

septcinq.to_sql('recipe', db, if_exists='replace', index = False)
print("inserted 750g data")

cuisine_az.to_sql('recipe', db, if_exists='replace', index = False)
print("inserted cuisine az data")

marieclaire.to_sql('recipe', db, if_exists='replace', index = False)
print("inserted marieclaire data")

