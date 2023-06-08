from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_file.db'

db = SQLAlchemy(app)

# ... define your models and routes ...

if __name__ == '__main__':
    app.run()
