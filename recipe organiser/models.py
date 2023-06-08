from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    ingredients = relationship("Ingredient", backref="recipe")

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe_rel = relationship("Recipe", backref="recipe_ingredients")
