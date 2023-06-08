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
@click.option('--name', prompt='Enter your name:')
@click.option('--description', prompt='Enter recipe description:')
def add_recipe(name, description):
    recipe = Recipe(name=name, description=description)
    session.add(recipe)
    session.commit()
    click.echo(f"Recipe '{recipe.name}' added successfully!")

@click.command()
def enter_ingredients():
    name = input('Enter your name: ')
    ingredients = input('Enter ingredients (comma-separated): ').split(',')

    # Query the database for recipes matching the entered ingredients
    query = session.query(Recipe).join(Ingredient).filter(Ingredient.name.in_(ingredients)).all()

    if query:
        click.echo("Recipes found:")
        for recipe in query:
            click.echo(f"- Recipe: {recipe.name}")
            click.echo(f"  Description: {recipe.description}")
    else:
        click.echo("No recipes found.")

cli.add_command(add_recipe)
cli.add_command(enter_ingredients)

if __name__ == '__main__':
    cli()
