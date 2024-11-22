from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Crea la aplicacion Flask

#Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://pokedex.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

#Conexion con la base de datos
db = SQLAlchemy(app)
#Ruta principal
@app.route('/')
def home():
    return jsonify({"message": "!Bienvenido a la Pokedex"})

@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    with open('data/pokemon.json') as f:
        pokemon_data = json.load(f)
    return jsonify(pokemon_data)

if __name__ == '__main__':
    app.run(debug=True)