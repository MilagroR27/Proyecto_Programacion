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
def obtener_todos_los_tipos(lista_pokemones):
    """
    Extrae y devuelve una lista con todos los tipos únicos del archivo JSON.
    """
    tipos_unicos = set()  # no acepta duplicados
    for pokemon in lista_pokemones:
        for tipo in pokemon["type"]:
            tipos_unicos.add(tipo)
    # list hace una lista. sorted la ordena alfabéticamente.
    return sorted(list(tipos_unicos))


def filtrar_por_multiples_tipos(lista_pokemones, mas_de_un_tipo):
    """
    Devuelve solo Pokémon con 1 tipo o con más de 1 tipo, según mas_de_un_tipo.
    """
    if mas_de_un_tipo:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) > 1]
    else:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) == 1]


def filtrar_por_tipo(lista_pokemones, tipo_buscado):
    """
    Devuelve los Pokémon que tengan el tipo indicado.
    """
    return [pokemon for pokemon in lista_pokemones if tipo_buscado in pokemon["type"]]


# DEBILIDADES
def es_debil_a(pokemon, tipo):
    """
    Devuelve True si el Pokémon es débil al tipo especificado.
    """
    return tipo in pokemon["weaknesses"]


def tiene_muchas_debilidades(pokemon):
    """
    Devuelve True si el Pokémon tiene más de 3 debilidades.
    """
    return len(pokemon["weaknesses"]) > 3


def descartar_por_debilidad(lista_pokemones, tipo):
    """
    Devuelve los Pokémon que SON débiles al tipo dado.
    """
    return [pokemon for pokemon in lista_pokemones if tipo in pokemon["weaknesses"]]


def descartar_por_muchas_debilidades(lista_pokemones):
    """
    Devuelve los Pokémon con 3 o más debilidades.
    """
    return [pokemon for pokemon in lista_pokemones if len(pokemon["weaknesses"]) >= 3]


# EVOLUCIÓN
def filtrar_por_evolucion(lista_pokemones, tiene_evolucion):
    """
    Si tiene_evolucion = True, devuelve los que tienen next_evolution.
    Si es False, devuelve los que NO tienen next_evolution.
    """
    if tiene_evolucion:
        return [pokemon for pokemon in lista_pokemones if "next_evolution" in pokemon]
    else:
        return [pokemon for pokemon in lista_pokemones if "next_evolution" not in pokemon]


def cantidad_evoluciones(pokemon):
    """
    Devuelve la cantidad de evoluciones siguientes.
    """
    if "next_evolution" in pokemon:
        return len(pokemon["next_evolution"])
    return 0


def filtrar_puede_evolucionar(lista_pokemones, puede):
    """
    Si puede = True, devuelve los que pueden evolucionar.
    Si False, los que no.
    """
    if puede:
        return [p for p in lista_pokemones if "next_evolution" in p]
    else:
        return [p for p in lista_pokemones if "next_evolution" not in p]


# ALTURA (conversión a número)
def filtrar_por_altura(lista_pokemones, minimo, maximo=None):
    """
    Filtra por altura en metros.
    minimo: altura mínima
    maximo: si se da, altura máxima
    """
    resultado = []
    for pokemon in lista_pokemones:
        altura = float(pokemon["height"].split()[0])  # "0.92 m" → 0.92
        if maximo is None:
            if altura >= minimo:
                resultado.append(pokemon)
        else:
            if minimo <= altura <= maximo:
                resultado.append(pokemon)
    return resultado


# PESO (conversión a número)
def filtrar_por_peso(lista_pokemones, minimo, maximo=None):
    """
    Filtra por peso en kg.
    minimo: peso mínimo
    maximo: si se da, peso máximo
    """
    resultado = []
    for pokemon in lista_pokemones:
        peso = float(pokemon["weight"].split()[0])  # "6.9 kg" → 6.9

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


def es_popular(pokemon):
    """
    Devuelve True si el Pokemon está en la lista POPULAR.
    """
    return pokemon["name"] in POPULAR


# esta funcion sirve para aceptar solo "si" o "no", si no hace un bucle
def preguntar(pregunta) -> bool:
    while True:
        respuesta = input(pregunta + "(si/no): " ).lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        print("responde solo con si o no")


def descartar_por_varios_tipos(lista_pokemones, mas_de_un_tipo):
    """
    Igual idea que filtrar_por_multiples_tipos, pero con otro nombre.
    """
    if mas_de_un_tipo:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) > 1]
    else:
        return [pokemon for pokemon in lista_pokemones if len(pokemon["type"]) == 1]


def descartar_por_tipo(lista_pokemones, tipo_buscado):
    """
    Devuelve una LISTA de Pokémon que tienen ese tipo.
    (Antes devolvía un set y eso rompía candidatos[0])
    """
    return [pokemon for pokemon in lista_pokemones if tipo_buscado in pokemon["type"]]


# Primera forma (no tiene prev_evolution)
def filtrar_por_primera_forma(lista_pokemones):
    return [p for p in lista_pokemones if "prev_evolution" not in p]


# Evolución intermedia (tiene prev y next)
def filtrar_por_forma_intermedia(lista_pokemones):
    return [p for p in lista_pokemones if "prev_evolution" in p and "next_evolution" in p]


# Evolución final (no tiene next_evolution)
def filtrar_por_forma_final(lista_pokemones):
    return [p for p in lista_pokemones if "next_evolution" not in p]
