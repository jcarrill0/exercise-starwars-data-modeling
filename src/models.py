import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    favorites = relationship('favorite', uselist=False, back_populates="parent")

class people(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(100))
    gender = Column(String(100))
    height = Column(Integer)
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    favorites = relationship('favorite')

class planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diamater = Column(Integer)
    favorites = relationship('favorite')

class favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship("user", back_populates="child")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')