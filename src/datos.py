import json  # Módulo para trabajar con archivos JSON

def cargar_pokedex():
    # Abre el archivo JSON y lo convierte en una estructura Python (diccionarios/listas)
    with open("./data/pokemon.json", "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    # Devuelve la lista de Pokémon dentro de la clave "pokemon"
    return data["pokemon"]
# BÚSQUEDA DE POKÉMON
# Devuelve el Pokémon cuyo número coincide con num_buscado.
def buscar_pokemon_por_num(lista_pokemones, num_buscado):
    for pokemon in lista_pokemones:
        if pokemon["num"] == num_buscado:
            return pokemon
    return None

# ------------------------------------
# FUNCIONES DE PREGUNTAS
# ------------------------------------
def preguntar_si_no(pregunta):
    """
    Hace una pregunta al usuario y solo acepta 'si' o 'no'.
    Devuelve True si la respuesta es 'si' y False si es 'no'.
    """
    while True:
        respuesta = input(pregunta + " (si/no): ").lower()

        if respuesta in ["si", "sí"]:
            return True
        if respuesta == "no":
            return False
        print("Responde solo con si o no.")

# TIPOS
# Devuelve True si el Pokémon es del tipo especificado.
def obtener_todos_los_tipos(lista_pokemones):
    """
    Extrae y devuelve una lista con todos los tipos únicos del archivo JSON.
    """
    tipos_unicos = set()
    
    for pokemon in lista_pokemones:
        for tipo in pokemon["type"]:
            tipos_unicos.add(tipo)
    return sorted(list(tipos_unicos))
""" 
preguntas como 
“¿Es de tipo Fuego?”
“¿Es de tipo Agua?”
"""

# Devuelve True si el Pokémon tiene más de un tipo.
# ¿Tiene más de un tipo?
def filtrar_por_multiples_tipos(lista_pokemones, mas_de_un_tipo):
    if mas_de_un_tipo:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) > 1]
    else:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) == 1]

def filtrar_por_tipo(lista_pokemones, tipo_buscado):
    return [pokemon for pokemon in lista_pokemones if tipo_buscado in pokemon["type"]]


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
def filtrar_por_evolucion(lista_pokemones, tiene_evolucion):
    if tiene_evolucion:
        return [pokemon for pokemon in lista_pokemones if "next_evolution" in pokemon]
    else:
        return [pokemon for pokemon in lista_pokemones if "next_evolution" not in pokemon]

# Devuelve la cantidad de evoluciones que tiene.
def cantidad_evoluciones(pokemon):
    if "next_evolution" in pokemon:
        return len(pokemon["next_evolution"])
    return 0

# ¿Puede evolucionar todavía?
def filtrar_puede_evolucionar(lista_pokemones, puede):
    if puede:
        return [p for p in lista_pokemones if "next_evolution" in p]
    else:
        return [p for p in lista_pokemones if "next_evolution" not in p]

# ALTURA (conversión a número)
def filtrar_por_altura(lista_pokemones, minimo, maximo=None):
    resultado = []
    for pokemon in lista_pokemones:
        altura = float(pokemon["height"].split()[0])  # Convierte "0.92 m" → 0.92
        if maximo is None:
            if altura >= minimo:
                resultado.append(pokemon)
        else:
            if minimo <= altura <= maximo:
                resultado.append(pokemon)
    return resultado

# PESO (conversión a número)
# Devuelve True si su peso es menor a 20 kg.
def filtrar_por_peso(lista_pokemones, minimo, maximo=None):
    resultado = []
    
    for pokemon in lista_pokemones:
        peso = float(pokemon["weight"].split()[0])  # Convierte "6.9 kg" → 6.9
        
        if maximo is None:
            if peso >= minimo:
                resultado.append(pokemon)
        else:
            if minimo <= peso <= maximo:
                resultado.append(pokemon)
    
    return resultado

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

# funciones debilidades

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

# Primera forma (no tiene prev_evolution)
def filtrar_por_primera_forma(lista_pokemones):
    return [p for p in lista_pokemones if "prev_evolution" not in p]


# Evolución intermedia (tiene prev y next)
def filtrar_por_forma_intermedia(lista_pokemones):
    return [p for p in lista_pokemones if "prev_evolution" in p and "next_evolution" in p]


# Evolución final (no tiene next_evolution)
def filtrar_por_forma_final(lista_pokemones):
    return [p for p in lista_pokemones if "next_evolution" not in p]
