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

@click.command(name='1', help=click.style('Add a recipe', fg='magenta'))
@click.option('--name', prompt=click.style('Enter recipe name:', fg='cyan'))
@click.option('--description', prompt=click.style('Enter recipe description:', fg='cyan'))
@click.option('--ingredients', prompt=click.style('Enter ingredients (comma-separated):', fg='cyan'))
@click.option('--instructions', prompt=click.style('Enter recipe instructions:', fg='cyan'))
def add_recipe(name, description, ingredients, instructions):
    recipe = Recipe(name=name, description=description, instructions=instructions)
    ingredient_list = [Ingredient(name=ingredient.strip()) for ingredient in ingredients.split(',')]
    recipe.ingredients.extend(ingredient_list)
    session.add(recipe)
    session.commit()
    click.echo(click.style(f"Recipe '{recipe.name}' added successfully!", fg='green'))

@click.command(name='2', help=click.style('Delete a recipe', fg='magenta'))
@click.option('--recipe-id', prompt=click.style('Enter recipe ID to delete:', fg='cyan'))
def delete_recipe(recipe_id):
    recipe = session.query(Recipe).get(recipe_id)
    if recipe:
        session.delete(recipe)
        session.commit()
        click.echo(click.style(f"Recipe '{recipe.name}' deleted successfully!", fg='green'))
    else:
        click.echo(click.style("Recipe not found.", fg='red'))

@click.command(name='3', help=click.style('Enter ingredients', fg='magenta'))
@click.option('--name', prompt=click.style('Enter your name:', fg='cyan'))
@click.option('--ingredients', prompt=click.style('Enter ingredients (comma-separated):', fg='cyan'))
def enter_ingredients(name, ingredients):
    # Query the database for recipes matching the entered ingredients
    query = session.query(Recipe).join(Ingredient).filter(Ingredient.name.in_(ingredients.split(','))).all()

    if query:
        click.echo(click.style("Recipes found:", fg='green'))
        for recipe in query:
            click.echo(click.style(f"- Recipe: {recipe.name}", fg='yellow'))
            click.echo(click.style(f"  Description: {recipe.description}", fg='yellow'))
            click.echo(click.style("  Instructions:", fg='yellow'))
            click.echo(recipe.instructions)
    else:
        click.echo(click.style("No recipes found.", fg='red'))

cli.add_command(add_recipe)
cli.add_command(delete_recipe)
cli.add_command(enter_ingredients)

if __name__ == '__main__':
    while True:
        click.echo(click.style("Select a command:", fg='blue'))
        click.echo(click.style("1. Add a recipe", fg='cyan'))
        click.echo(click.style("2. Delete a recipe", fg='cyan'))
        click.echo(click.style("3. Enter ingredients", fg='cyan'))
        command = click.prompt(click.style("Enter command number (or 'q' to quit)", fg='cyan'))

        if command == 'q':
            break

        try:
            cli.commands[command]()
        except KeyError:
            click.echo(click.style("Invalid command. Please select a valid command number.", fg='red'))
