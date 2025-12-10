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




#hola


def descartar_por_devilidad(lista_pokemones,tipo):
    return [pokemon for pokemon in lista_pokemones if tipo in pokemon["weaknesses"]]

def descartar_por_muchas_debilidades(lista_pokemones):
    return [pokemon for pokemon in lista_pokemones if len(pokemon["weaknesses"]) >= 3 ]


# esta funcion sirve para aceptar solo "si" o "no", si no hace un bucle 

def preguntar(pregunta) -> bool:
    while True:
        respuesta = input(pregunta + "(si/no): " ).lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        print("responde solo con si o no")

# esta funcion son va a servir para preguntar por los tipos 
def obtener_todos_los_tipos(lista_pokemones):
    # extrae todos los tipos unicos del archivo json
    tipos_unicos = set() #no acepta duplicados
    for pokemon in lista_pokemones:
        for tipo in pokemon["type"]:
            tipos_unicos.add(tipo) #guarda los tipos de cada pokemon
    return sorted(list(tipos_unicos)) 
    # list hace una lista. sorted la ordenada alfabeticamente. tipos_unicos es un set no tiene orden 


def descartar_por_varios_tipos(lista_pokemones, mas_de_un_tipo):
    if mas_de_un_tipo:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) > 1]
    else:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) == 1]
    

def descartar_por_tipo(lista_pokemones, tipo_buscado):
    return {pokemon for pokemon in lista_pokemones if tipo_buscado in pokemon["type"]}


