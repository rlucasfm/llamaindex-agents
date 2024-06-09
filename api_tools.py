import requests
from llama_index.core.tools import FunctionTool

def search_pokemon(pokemon_name):
    api_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name.lower()
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()

    return "Can't find this pokemon"

pokemon_engine = FunctionTool.from_defaults(
    fn=search_pokemon,
    name="pokemon_finder",
    description="this tool can find data about any pokemon"
)