import click
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


@click.group()
def cli():
    pass


@cli.command()
def greet():
    name = click.prompt("Enter your name")
    click.echo(f"Hello, {name}!")


@cli.command()
def enter_ingredients():
    name = click.prompt("Enter your name")
    ingredients_input = click.prompt("Enter ingredients (comma-separated)")
    ingredients_list = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    generate_recipes(name, ingredients_list)


def generate_recipes(name, ingredients):
    session = Session()
    query = session.query(Recipe).join(Ingredient).filter(Ingredient.name.in_(ingredients)).all()
    if query:
        click.echo(f"Hello, {name}!")
        click.echo("Based on your ingredients, here are some recipes you can try:")
        for recipe in query:
            click.echo(f"Recipe: {recipe.name}")
            click.echo(f"Description: {recipe.description}")
            click.echo("------")
    else:
        click.echo("No recipes found for the given ingredients.")
    session.close()


@cli.command()
def add_recipe():
    name = click.prompt("Enter your name")
    recipe_name = click.prompt("Enter recipe name")
    recipe_description = click.prompt("Enter recipe description")
    session = Session()
    recipe = Recipe(name=recipe_name, description=recipe_description)
    session.add(recipe)
    session.commit()

    click.echo("Enter ingredients for the recipe (comma-separated)")
    ingredients_input = click.prompt("Ingredients")
    ingredients_list = [ingredient.strip() for ingredient in ingredients_input.split(",")]

    for ingredient_name in ingredients_list:
        ingredient = Ingredient(name=ingredient_name, recipe=recipe)
        session.add(ingredient)
    session.commit()

    click.echo("Recipe and ingredients added successfully.")
    session.close()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    cli()

