import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Recipe, Ingredient

# Connect to the SQLite database file
engine = create_engine('sqlite:///recipes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create the necessary tables if they don't exist
Base.metadata.create_all(engine)

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', prompt='Enter recipe name:')
@click.option('--description', prompt='Enter recipe description:')
@click.option('--ingredients', prompt='Enter ingredients (comma-separated):')
@click.option('--instructions', prompt='Enter recipe instructions:')
def add_recipe(name, description, ingredients, instructions):
    recipe = Recipe(name=name, description=description, instructions=instructions)
    ingredient_list = [Ingredient(name=ingredient.strip()) for ingredient in ingredients.split(',')]
    recipe.ingredients.extend(ingredient_list)
    session.add(recipe)
    session.commit()
    click.echo(f"Recipe '{recipe.name}' added successfully!")

@click.command()
@click.option('--name', prompt='Enter your name:')
@click.option('--ingredients', prompt='Enter ingredients (comma-separated):')
def enter_ingredients(name, ingredients):
    # Query the database for recipes matching the entered ingredients
    query = session.query(Recipe).join(Ingredient).filter(Ingredient.name.in_(ingredients.split(','))).all()

    if query:
        click.echo("Recipes found:")
        for recipe in query:
            click.echo(f"- Recipe: {recipe.name}")
            click.echo(f"  Description: {recipe.description}")
            click.echo(f"  Instructions:")
            click.echo(recipe.instructions)
    else:
        click.echo("No recipes found.")

@click.command()
@click.option('--name', prompt='Enter recipe name:')
def delete_recipe(name):
    recipe = session.query(Recipe).filter_by(name=name).first()
    if recipe:
        session.delete(recipe)
        session.commit()
        click.echo(f"Recipe '{name}' deleted successfully!")
    else:
        click.echo(f"Recipe '{name}' not found.")

cli.add_command(add_recipe)
cli.add_command(enter_ingredients)
cli.add_command(delete_recipe)

if __name__ == '__main__':
    cli()

