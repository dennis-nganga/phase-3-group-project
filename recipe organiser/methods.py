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
