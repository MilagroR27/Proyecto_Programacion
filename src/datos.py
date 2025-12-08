import json  # Módulo para trabajar con archivos JSON

def cargar_pokedex():
    # Abre el archivo JSON y lo convierte en una estructura Python (diccionarios/listas)
    with open("./data/pokemon.json", "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    # Devuelve la lista de Pokémon dentro de la clave "pokemon"
    return data["pokemon"]

# TIPOS
# Devuelve True si el Pokémon es del tipo especificado.
def es_de_tipo(pokemon, tipo):
    return tipo in pokemon["type"]
""" 
preguntas como 
“¿Es de tipo Fuego?”
“¿Es de tipo Agua?”
"""

# Devuelve True si el Pokémon tiene más de un tipo.
def tiene_mas_de_un_tipo(pokemon):
    return len(pokemon["type"]) > 1

# DEBILIDADES
# Devuelve True si el Pokémon es débil al tipo especificado.
def es_debil_a(pokemon, tipo):
    return tipo in pokemon["weaknesses"]
"""
preguntas como 
“¿Es débil al tipo Eléctrico?”
“¿Es débil al tipo Agua?”
“¿Es débil al tipo Hielo?”
"""

# Devuelve True si el Pokémon tiene más de 3 debilidades.
def tiene_muchas_debilidades(pokemon):
    return len(pokemon["weaknesses"]) > 3

# EVOLUCIÓN
# Devuelve True si el Pokémon puede evolucionar (tiene evolución siguiente).
def puede_evolucionar(pokemon):
    return "next_evolution" in pokemon
"""
“¿Puede evolucionar todavía?”
"""

# Devuelve True si NO tiene prev_evolution (es la primera forma).
def es_primera_forma(pokemon):
    return "prev_evolution" not in pokemon
"""
“¿Es su primera forma?”
"""

# Devuelve la cantidad de evoluciones que tiene.
def cantidad_evoluciones(pokemon):
    if "next_evolution" in pokemon:
        return len(pokemon["next_evolution"])
    return 0

# ALTURA (conversión a número)
# Devuelve True si su altura es menor a 1 metro.
def es_bajo(pokemon):
    altura = float(pokemon["height"].split(" ")[0])
    return altura < 1

"""
# Devuelve True si su altura está entre 1 y 1.5 metros.
def es_intermedio(pokemon):
    altura = float(pokemon["height"].split(" ")[0])
    return 1 <= altura <= 1.5

# Devuelve True si su altura es mayor a 1.5 metros.
def es_alto(pokemon):
    altura = float(pokemon["height"].split(" ")[0])
    return altura > 1.5
"""

# PESO (conversión a número)
# Devuelve True si su peso es menor a 20 kg.
def es_liviano(pokemon):
    peso = float(pokemon["weight"].split(" ")[0])
    return peso < 20

# POPULARIDAD
POPULAR = [
    "Bulbasaur", "Ivysaur", "Venusaur",
    "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise",
    "Pikachu"
]

# Devuelve True si el Pokémon es considerado popular.
def es_popular(pokemon):
    return pokemon["name"] in POPULAR