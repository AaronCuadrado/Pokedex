from flask import Flask, jsonify

app = Flask(__name__)

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