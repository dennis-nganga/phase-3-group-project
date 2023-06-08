from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///meal_database.db')
Session = sessionmaker(bind=engine)
