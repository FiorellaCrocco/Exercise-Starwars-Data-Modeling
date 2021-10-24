import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorite_character = db.relationship('FavoriteCharacter', backref='user', lazy=True)
    favorite_planet = db.relationship('Favorite_Planet', backref="user" , lazy=True)

class Character(Base):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    favorite_character = db.relationship('FavoriteCharacter', backref='character', lazy=True)

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "gender":self.gender,
            "hair_color":self.hair_color,
            "eye_color":self.eye_color,
            "height":self.height,
            "mass":self.mass,
            "skin_color":self.skin_color,
            "birth_year":self.birth_year
        }

class Planet(Base):
    __tablename__ = 'planet'   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.String(80), unique=False, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    surface_water = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    favorite_planet = db.relationship('Favorite_Planet', backref="planet" , lazy=True)

        def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "rotation_period":self.rotation_period,
            "orbital_period":self.orbital_period,
            "diameter":self.diameter,
            "climate":self.climate,
            "gravity":self.gravity,
            "terrain":self.terrain,
            "surface_water":self.surface_water,
            "population":self.population
        }


class FavoriteCharacter(Base):
    __tablename__ = 'FavoriteCharacter'   
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def to_dict(self):
    return {
        "id":self.id,
        "user_id":self.user_id,
        "character_id":self.character_id
    }

class Favorite_Planet(Base):
    __tablename__ = 'Favorite_Planet'   
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def to_dict(self):
    return {
        "user_id":self.user_id,
        "planet_id":self.character_id
    } 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')