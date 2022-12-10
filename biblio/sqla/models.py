import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.ext.automap import automap_base
# Base = declarative_base()

from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"])
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

print('hey', Base.classes.keys())
Recipe = Base.classes.recipe

# class Recipe(DeferredReflection, Base):
#     __tablename__ = 'recipe'
