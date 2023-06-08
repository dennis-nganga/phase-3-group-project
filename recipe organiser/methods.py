from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Ingredient
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Create the database engine
engine = create_engine('sqlite:///recipes.db')
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

def create_database():
    """Create the database and tables if they don't exist."""
    Base.metadata.create_all(engine)
    print("Database created successfully.")

def add_ingredient():
    name = input("Enter ingredient name: ")
    quantity = input("Enter ingredient quantity: ")
    ingredient = Ingredient(name=name, quantity=quantity)
    session.add(ingredient)
    session.commit()
    print("Ingredient added successfully.")

def display_ingredients():
    ingredients = session.query(Ingredient).all()
    if ingredients:
        for ingredient in ingredients:
            print(ingredient)
    else:
        print("No ingredients found.")

def run_cli():
    while True:
        print("\n=== Recipe Generator CLI ===")
        print("1. Add Ingredient")
        print("2. Display Ingredients")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_ingredient()
        elif choice == "2":
            display_ingredients()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
class Recipe(Base):
    # ... class definition ...

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        return f"<Recipe(name='{self.name}')>"

    def add_ingredient(self, ingredient):
        # Add an ingredient to the recipe
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        # Remove an ingredient from the recipe
        self.ingredients.remove(ingredient)

    def get_ingredient_names(self):
        # Return a list of ingredient names
        return [ingredient.name for ingredient in self.ingredients]

    def to_dict(self):
        # Return a dictionary representation of the recipe
        return {
            'name': self.name,
            'ingredients': self.get_ingredient_names()
        }

    @classmethod
    def from_dict(cls, recipe_dict):
        # Create a Recipe object from a dictionary
        name = recipe_dict.get('name')
        ingredients = recipe_dict.get('ingredients', [])
        return cls(name, ingredients)
if __name__ == "__main__":
    run_cli()