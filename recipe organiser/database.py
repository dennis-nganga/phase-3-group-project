from sqlalchemy.orm import sessionmaker
from models import Meal, HealthFact, Ingredient, Recipe, engine

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

def add_recipes():
    # Coffee recipe
    coffee = Recipe(name='Coffee', description='A simple recipe for making coffee')
    coffee.ingredients = [
        Ingredient(name='Coffee beans'),
        Ingredient(name='Water'),
        Ingredient(name='Sugar (optional)'),
        Ingredient(name='Milk (optional)')
    ]
    session.add(coffee)

    # Sandwich recipe
    sandwich = Recipe(name='Sandwich', description='A classic sandwich recipe')
    sandwich.ingredients = [
        Ingredient(name='Bread slices'),
        Ingredient(name='Cheese slices'),
        Ingredient(name='Sliced ham'),
        Ingredient(name='Lettuce'),
        Ingredient(name='Tomato slices'),
        Ingredient(name='Mayonnaise'),
        Ingredient(name='Mustard')
    ]
    session.add(sandwich)

    # Fries recipe
    fries = Recipe(name='Fries', description='Homemade french fries recipe')
    fries.ingredients = [
        Ingredient(name='Potatoes'),
        Ingredient(name='Vegetable oil'),
        Ingredient(name='Salt')
    ]
    session.add(fries)

    session.commit()
    print("Recipes added successfully!")


if __name__ == '__main__':
    add_recipes()

