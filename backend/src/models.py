from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Type(db.Model):
    __tablename__= 'types' #Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(200), nullable=False)

    pokemons = db.relationship('PokemonType', back_populates='type')

class Pokemon(db.Model):
    __tablename__= 'pokemon'
    id = db.CColumn(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)

    types = db.relationship('PokemonType', back_populates='pokemon')

class PokemonType(db.Model):
    __tablename__='pokemon_types'
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)

    pokemon = db.relationship('Pokemon', back_populates='types')
    type = db.relationship('Type', back_populates='pokemons')
