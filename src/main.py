from datos import (
    cargar_pokedex,
    es_de_tipo,
    tiene_mas_de_un_tipo,
    tiene_muchas_debilidades,
    puede_evolucionar,
    es_primera_forma,
    es_bajo,
    es_liviano,
    es_popular
)

pokedex = cargar_pokedex()
#lambda permite crear funciones pequeñas en una sola línea, sin usar def
preguntas = [
    {"texto": "¿Puede evolucionar todavía?", "condicion": lambda pokemon: puede_evolucionar(pokemon)},
    {"texto": "¿Es de tipo Agua?", "condicion": lambda pokemon: es_de_tipo(pokemon, "Water")},
    {"texto": "¿Es de tipo Fuego?", "condicion": lambda pokemon: es_de_tipo(pokemon, "Fire")},
    {"texto": "¿Tiene más de un tipo?", "condicion": lambda pokemon: tiene_mas_de_un_tipo(pokemon)},
    {"texto": "¿Es liviano? (menos de 20 kg)", "condicion": lambda pokemon: es_liviano(pokemon)},
    {"texto": "¿Es su primera forma?", "condicion": lambda pokemon: es_primera_forma(pokemon)},
    {"texto": "¿Es bajo? (menos de 1 metro)", "condicion": lambda pokemon: es_bajo(pokemon)},
    {"texto": "¿Es popular?", "condicion": lambda pokemon: es_popular(pokemon)},
]
candidatos = pokedex[:]  # [:] copia de todos los Pokémon de manera independiente

print("¿Es de tipo Agua?")
respuesta = input("(si/nn): ").lower()
#Es una "list comprehension" es para hacer una lista mas compacta
#Crea una nueva lista con los Pokémon en candidatos que sean de tipo agua, y reemplazamos a candidatos con esa lista.
if respuesta == "si":
    candidatos = [pokemon for pokemon in candidatos if es_de_tipo(pokemon, "Water")]
else:
    candidatos = [pokemon for pokemon in candidatos if not es_de_tipo(pokemon, "Water")]

print("Pokémon posibles:")
for pokemon in candidatos[:10]:  # Mostramos solo los primeros 10
    print("-", pokemon["name"])

print(f"Total: {len(candidatos)}")
"""print("Total de Pokémon cargados:", len(pokedex))
print(pokedex[0])
print("Primer Pokémon:", pokedex[0]["name"])
print("Tipos:", pokedex[0]["type"])

for pokemon in pokedex[:5]:
    if tipo(pokemon, "Water"):
        print(pokemon["name"], "es de tipo Agua")
    else:
        print(pokemon["name"], "NO es de tipo Agua")"""
