from datos import (
    cargar_pokedex,
    obtener_todos_los_tipos,
    filtrar_por_peso,
    es_popular, preguntar,
    descartar_por_tipo, 
    filtrar_por_multiples_tipos,
    descartar_por_devilidad,
    filtrar_por_tipo,
    obtener_todos_los_tipos,
    buscar_pokemon_por_num,
    preguntar_si_no
)

pokedex = cargar_pokedex()
#lambda permite crear funciones pequeñas en una sola línea, sin usar def
# cambiar las preguntas
"""preguntas = [
    {"texto": "¿Puede evolucionar todavía?", "condicion": lambda pokemon: puede_evolucionar(pokemon)},
    {"texto": "¿Es de tipo Agua?", "condicion": lambda pokemon: obtener_todos_los_tipos(pokemon, "Water")},
    {"texto": "¿Es de tipo Fuego?", "condicion": lambda pokemon: obtener_todos_los_tipos(pokemon, "Fire")},
    {"texto": "¿Tiene más de un tipo?", "condicion": lambda pokemon: tiene_mas_de_un_tipo(pokemon)},
    {"texto": "¿Es liviano? (menos de 20 kg)", "condicion": lambda pokemon: filtrar_por_peso(pokemon)},
    {"texto": "¿Es su primera forma?", "condicion": lambda pokemon: es_primera_forma(pokemon)},
    {"texto": "¿Es bajo? (menos de 1 metro)", "condicion": lambda pokemon: es_bajo(pokemon)},
    {"texto": "¿Es popular?", "condicion": lambda pokemon: es_popular(pokemon)},
]"""
candidatos = pokedex[:]  # [:] copia de todos los Pokémon de manera independiente

"""print("¿Es de tipo Agua?")
respuesta = input("(si/nn): ").lower()
#Es una "list comprehension" es para hacer una lista mas compacta
#Crea una nueva lista con los Pokémon en candidatos que sean de tipo agua, y reemplazamos a candidatos con esa lista.
if respuesta == "si":
    candidatos = [pokemon for pokemon in candidatos if obtener_todos_los_tipos(pokemon, "Water")]
else:
    candidatos = [pokemon for pokemon in candidatos if not obtener_todos_los_tipos(pokemon, "Water")]

print("Pokémon posibles:")
for pokemon in candidatos[:10]:  # Mostramos solo los primeros 10
    print("-", pokemon["name"])

print(f"Total: {len(candidatos)}")"""
"""print("Total de Pokémon cargados:", len(pokedex))
print(pokedex[0])
print("Primer Pokémon:", pokedex[0]["name"])
print("Tipos:", pokedex[0]["type"])

for pokemon in pokedex[:5]:
    if tipo(pokemon, "Water"):
        print(pokemon["name"], "es de tipo Agua")
    else:
        print(pokemon["name"], "NO es de tipo Agua")"""

#------------------------------------


print(" piensa en un pokemon \n")

# sirve para obtener todos los tipos unicos del archivo sin repetirse
tipos_disponibles = obtener_todos_los_tipos(candidatos)

# PREGUNTAS POR TIPO 

for tipo in tipos_disponibles:
    if len(candidatos) <= 1:
        break
    elif preguntar(f"tu pokemon es tipo {tipo}"):
        candidatos = descartar_por_tipo(candidatos,tipo)

# RESULTADO FINAL

print("\n Pokemones posibles: ", len(candidatos))
print("\n")

if len(candidatos) == 1:
    print("tu pokemon es " + candidatos[0]["name"])
elif len(candidatos) > 1:
    for pokemon in candidatos:
        print(pokemon["name"])
else:
    print("no encontre ningun pokemon con esas caracteristicas")
#-------------------------

num = input("Ingresa el número Pokédex (ej: 025): ")
pokemon = buscar_pokemon_por_num(pokemon, num)

if pokemon:
    print("Nombre:", pokemon["name"])
    print("Tipos:", ", ".join(pokemon["type"]))
    print("Debilidades:", ", ".join(pokemon["weaknesses"]))
else:
    print("Pokémon no encontrado.")






# ------------------------------------
# OBTENER TIPOS ÚNICOS
# ------------------------------------




"""# ¿Tiene más de un tipo?  NUEVO
def filtrar_por_multiples_tipos(lista_pokemones, mas_de_un_tipo):
    if mas_de_un_tipo:
        return [p for p in lista_pokemones if len(p["type"]) > 1]
    else:
        return [p for p in lista_pokemones if len(p["type"]) == 1]
"""







# ------------------------------------
# SISTEMA PRINCIPAL - AKINATOR POKÉMON
# ------------------------------------

candidatos = pokemon[:]  # Copia de los pokemones disponibles

print("¡Piensa en un Pokémon! Voy a intentar adivinarlo.\n")

# Obtener tipos únicos del archivo
tipos_disponibles = obtener_todos_los_tipos(candidatos)


# ---------------------------
# PREGUNTAS AUTOMÁTICAS POR TIPO
# ---------------------------

# ---------------------------
# ¿TIENE MÁS DE UN TIPO?     NUEVO
# ---------------------------
#PREGUNTA SOBRE SI TIENE EVOLUCIÓN
if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon tiene evoluciones?"):
        candidatos = filtrar_por_evolucion(candidatos, True)
    else:
        candidatos = filtrar_por_evolucion(candidatos, False)


if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon tiene más de un tipo?"):
        cantidad_tipos = 2
    else:
        cantidad_tipos = 1

tipos_encontrados = 0

for tipo in tipos_disponibles:
    if len(candidatos) <= 1:
        break
    if tipos_encontrados >= cantidad_tipos:
        break  # ya preguntamos todos los tipos necesarios
    if preguntar_si_no(f"¿Tu Pokémon es tipo {tipo}?"):
        candidatos = filtrar_por_tipo(candidatos, tipo)
        tipos_encontrados += 1

# ¿Puede evolucionar todavía?   NUEVO
if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon puede evolucionar todavía?"):
        candidatos = filtrar_puede_evolucionar(candidatos, True)
    else:
        candidatos = filtrar_puede_evolucionar(candidatos, False)

# ---------------------------
# TIPO DE EVOLUCIÓN (EXCLUYENTE)
# ---------------------------
if len(candidatos) > 1:

    if preguntar_si_no("¿Tu Pokémon es la primera forma de su línea evolutiva?"):
        candidatos = filtrar_por_primera_forma(candidatos)

    elif preguntar_si_no("¿Es una evolución intermedia? (tiene forma previa y puede evolucionar)"):
        candidatos = filtrar_por_forma_intermedia(candidatos)

    elif preguntar_si_no("¿Es una evolución final? (no puede evolucionar más)"):
        candidatos = filtrar_por_forma_final(candidatos)

# ---------------------------
# ALTURA INTELIGENTE
# ---------------------------
if len(candidatos) > 1:
    if preguntar_si_no("¿Mide más de 1 metro?"):
        candidatos = filtrar_por_altura(candidatos, 1.0)
    else:
        candidatos = filtrar_por_altura(candidatos, 0.0, 1.0)

# ---------------------------
# PESO INTELIGENTE
# ---------------------------
if len(candidatos) > 1:
    if preguntar_si_no("¿Pesa más de 20 kg?"):
        candidatos = filtrar_por_peso(candidatos, 20.0)
    else:
        candidatos = filtrar_por_peso(candidatos, 0.0, 20.0)

# ---------------------------
# DEBILIDADES
# ---------------------------

# ---------------------------
# ¿TIENE MUCHAS DEBILIDADES?
# ---------------------------
if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon es débil a 3 o más tipos?"):
        max_debilidades = 3
    else:
        max_debilidades = 2

debilidades_comunes = ["Fighting", "Electric", "Ice", "Water", "Poison", "Rock", "Psychic","Fire","Ground"]

debilidades_encontradas = 0

for debilidad in debilidades_comunes:
    if len(candidatos) <= 1:
        break
    if debilidades_encontradas >= max_debilidades:
        break  # ya se encontraron las necesarias

    if preguntar_si_no(f"¿Tu Pokémon es débil al tipo {debilidad}?"):
        candidatos = filtrar_por_debilidad(candidatos, debilidad)
        debilidades_encontradas += 1



# ------------------------------------
# RESULTADO FINAL
# ------------------------------------
print("\n---------------------------------")
print("Pokémon posibles:", len(candidatos))
print("---------------------------------\n")

if len(candidatos) == 1:
    print("¡Creo que tu Pokémon es... 👉 " + candidatos[0]["name"] + "!")
elif len(candidatos) > 1:
    print("No estoy seguro, pero podrían ser estos:")
    for pokemon in candidatos:
        print("-", pokemon["name"])
else:
    print("No encontré ningún Pokémon con esas características.")
