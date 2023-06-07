from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the database engine
engine = create_engine('sqlite:///recipes.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create the base class for declarative models
Base = declarative_base()

# Define the Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = relationship("Ingredient", back_populates="recipe")

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship("Recipe", back_populates="ingredients")

# Function to generate recipes based on available ingredients
def generate_recipe(available_ingredients):
    # Query the database for recipes containing any of the available ingredients
    recipes = session.query(Recipe).join(Recipe.ingredients).filter(Ingredient.name.in_(available_ingredients)).all()

    if not recipes:
        print("No recipes found with the given ingredients.")
        return

    print("Recipes:")
    for recipe in recipes:
        print(f"- {recipe.name}")
        print(f"  Ingredients: {[ingredient.name for ingredient in recipe.ingredients]}")
        print()

# Example usage
available_ingredients = input("Enter the ingredients you have (comma-separated): ").split(',')
generate_recipe(available_ingredients)