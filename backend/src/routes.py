from flask import Blueprint, jsonify, request
from src.models import Pokemon, Type

routes = Blueprint('routes', __name__)

#Ruta para obtener todos los pokemon
@routes.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    paginated_pokemons = Pokemon.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total": paginated_pokemons.total,
        "page": paginated_pokemons.page,
        "pages": paginated_pokemons.pages,
        "results": [
            {
                "id": p.id,
                "name": p.name,
                "image": p.image,
                "types": [
                    {"name": t.type.name, "image": t.type.image}
                    for t in p.types
                ]
            } for p in paginated_pokemons.items
        ]
    })

@routes.route('/api/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    pokemon = Pokemon.query.get_or_404(pokemon_id)
    return jsonify({
        "id": pokemon.id,
        "name": pokemon.name,
        "image": pokemon.image,
        "types": [
            {"name": t.type.name, "image": t.type.image}
            for t in pokemon.types
        ]
    })

# Listar tipos
@routes.route('/api/types', methods=['GET'])
def get_types():
    types = Type.query.all()
    return jsonify([
        {"name": t.name, "image": t.image} for t in types
    ])