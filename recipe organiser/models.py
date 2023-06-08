from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Add additional attributes as needed for the Meal class


class HealthFact:
    def __init__(self, meal):
        self.meal = meal
        self.engine = create_engine('sqlite:///meal_database.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def check_healthiness(self):
        unhealthy_ingredients = ["fried", "processed", "sugary", "high-fat"]
        unhealthy_count = 0

        for ingredient in self.meal.ingredients:
            for unhealthy in unhealthy_ingredients:
                if unhealthy in ingredient:
                    unhealthy_count += 1

        if unhealthy_count > len(self.meal.ingredients) // 2:
            return False
        return True

    def get_health_fact(self):
        if self.check_healthiness():
            return "This meal is healthy and nutritious!"
        else:
            return "Warning: This meal may not be healthy. Consider making healthier ingredient choices."

    def save_meal_to_database(self):
        meal = Meal(name=self.meal.name)
        # Set other attributes of the meal object as needed
        self.session.add(meal)
        self.session.commit()
        self.session.close()

    def load_meals_from_database(self):
        meals = self.session.query(Meal).all()
        for meal in meals:
            print(meal.name)
        self.session.close()


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    recipe = relationship("Recipe", backref="ingredients")

    def __repr__(self):
        return f'Ingredient: {self.name}'


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = relationship("Ingredient", backref="recipe")


# Create the database engine
engine = create_engine('sqlite:///recipes.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create the base class for declarative models
Base.metadata.create_all(engine)
