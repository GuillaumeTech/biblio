from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeferredReflection
Base = declarative_base()

class Recipe(DeferredReflection, Base):
    __tablename__ = 'recipe'