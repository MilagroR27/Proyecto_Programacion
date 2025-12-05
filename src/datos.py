import json #importamos el json

def cargar_pokedex():
    with open("./data/pokemon.json", "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return data["pokemon"]
