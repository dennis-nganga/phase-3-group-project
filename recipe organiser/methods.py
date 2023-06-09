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

@click.command(name='1', help='Add a recipe')
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

@click.command(name='2', help='Delete a recipe')
@click.option('--recipe-id', prompt='Enter recipe ID to delete:')
def delete_recipe(recipe_id):
    recipe = session.query(Recipe).get(recipe_id)
    if recipe:
        session.delete(recipe)
        session.commit()
        click.echo(f"Recipe '{recipe.name}' deleted successfully!")
    else:
        click.echo("Recipe not found.")

@click.command(name='3', help='Enter ingredients')
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

cli.add_command(add_recipe)
cli.add_command(delete_recipe)
cli.add_command(enter_ingredients)

if __name__ == '__main__':
    while True:
        click.echo("Select a command:")
        click.echo("1. Add a recipe")
        click.echo("2. Delete a recipe")
        click.echo("3. Enter ingredients")
        command = click.prompt("Enter command number (or 'q' to quit)")

        if command == 'q':
            break

        try:
            cli.commands[command]()
        except KeyError:
            click.echo("Invalid command. Please select a valid command number.")

