## Recipe Management System
The Recipe Management System is a Python-based application that allows users to organize and manage their recipes effectively. It provides features for adding ingredients, creating recipes, and maintaining a database of meals and their associated health facts. This system helps users make informed decisions about their meals and promotes healthier eating habits.

## Features
Ingredient Management: Add and manage ingredients for your recipes, including name and quantity information.
Recipe Creation: Create recipes by combining ingredients and specifying their quantities.
Meal Database: Maintain a database of meals, including their names and associated health facts.
Health Fact Evaluation: Evaluate the healthiness of a meal based on the presence of unhealthy ingredients.
Database Persistence: Store and retrieve data using the SQLite database engine.
Command-Line Interface (CLI): Interact with the system through a user-friendly command-line interface.
## Prerequisites
To run the Recipe Management System, you need the following prerequisites:

Python 3.6 or later installed on your system.
Required Python packages: sqlalchemy, sqlite3, and any other dependencies listed in the requirements.txt file.
Access to the SQLite database engine.
## Installation and Setup
1. Clone the repository:

git clone https://github.com/your-username/recipe-management-system.git

2. Navigate to the project directory:

cd recipe-management-system

3. Install the required Python packages:

pip install -r requirements.txt

4. Create the database and tables:

python methods.py create_database
5. Start the Recipe Management System:

python methods.py run_cli

## Usage
1. Add Ingredients: Use the CLI to add ingredients and specify their names and quantities.

2. Create Recipes: Combine ingredients and specify their quantities to create recipes.

3. Evaluate Health Facts: The system will evaluate the healthiness of a meal based on the presence of unhealthy ingredients.

4. Display Ingredients: View a list of all ingredients stored in the system.

5. Exit the CLI: Enter 0 in the CLI to exit the system.

## Contributing
Contributions to the Recipe Management System are welcome! If you find any issues or have suggestions for enhancements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.

## Acknowledgments
1. SQLAlchemy - Python SQL toolkit and ORM that provides a powerful and flexible way to interact with databases.
2. SQLite - A self-contained, serverless database engine that is widely used for embedded systems and small-scale applications.
3. Click - A Python package that provides a simple and intuitive command-line interface creation utility, used in this code for creating CLI commands and options




