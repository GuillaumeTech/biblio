import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.ext.automap import automap_base

from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"])
Base = automap_base()
Base.prepare(autoload_with=engine)

Recipe = Base.classes.recipe
