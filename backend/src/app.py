from flask import Flask, jsonify
from flask_sqlalchemy import SQL
from flask_migrate import MigrateAlchemy, Migrate
from src.models import db, Pokemon, Type

app = Flask(__name__) #Crea la aplicacion Flask

#Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db.init_app(app)

migrate = Migrate(app, db)

#Ruta principal
@app.route('/')
def home():
    return jsonify({"message": "!Bienvenido a la Pokedex"})

@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    pokemons = Pokemon.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "image": p.image,
            "types": [
                {"name": t.type.name, "image": t.type.image}
                for t in p.types
            ]
        } for p in pokemons
    ])

#Ruta para obtener todos los tipos
@app.route('/api/types', methods=['GET'])
def get_types():
    types = Type.query.all()
    return jsonify([
        {"name": t.name, "image": t.image} for t in types
    ])

if __name__ == '__main__':
    app.run(debug=True)