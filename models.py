from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
      __tablename__ = 'users'
      id = Column(Integer, primary_key=True)
      name = Column(String(50), nullable=False)
      role = Column(String(50), default="beginner")    # Beginner/Chef/Collector

class Ingredient(Base):
      __tablename__ = 'ingredients'
      id = Column(Integer, primary_key=True)
      name = Column(String(100), nullable=False)
      unit = Column(String(50))    # Граммы, литры, штуки...

class Recipe(Base):
      __tablename__ = 'recipes'
      id = Column(Integer, primary_key=True)
      title = Column(String(100), nullable=False)
      instruction = Column(Text, nullable=False)
      prep_time = Column(Integer, nullable=False)    # В минутах
      category = Column(String(50), nullable=False)    # Appetizer, Main course, Dessert
      created_at = Column(DateTime, default=datetime.now())
      updated_at = Column(DateTime, onupdate=datetime.now())
      user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class Comment(Base):
      __tablename__ = 'comments'
      id = Column(Integer, primary_key=True)
      text = Column(Text, nullable=False)
      user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
      recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

class Image(Base):
      __tablename__ = 'images'
      id = Column(Integer, primary_key=True)
      path = Column(String(255), nullable=False)
      recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

class HistoryAction(Base):
      __tablename__ = 'history_actions'
      id = Column(Integer, primary_key=True)
      action_type = Column(String(50), nullable=False)    # Create, Edit, Delete
      timestamp = Column(DateTime, default=datetime.now(), nullable=False)
      user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
      object_id = Column(Integer, nullable=False)    # ID объекта (рецепт, комментарий...)

engine = create_engine('sqlite:///recipes.db')
Base.metadata.create_all(engine)