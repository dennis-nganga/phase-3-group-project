from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///meal_database.db')
Session = sessionmaker(bind=engine)


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    ingredients = relationship("Ingredient", backref="recipe_ingredients")


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))


Base.metadata.create_all(engine)
