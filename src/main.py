from datos import (
    cargar_pokedex,
    obtener_todos_los_tipos,
    filtrar_por_peso,
    filtrar_por_tipo,
    preguntar_si_no,
    filtrar_puede_evolucionar,
    filtrar_por_evolucion,
    filtrar_por_primera_forma,
    filtrar_por_altura,
    filtrar_por_forma_intermedia,
    filtrar_por_forma_final,
    es_debil_a, 
    es_popular, 
)

pokedex = cargar_pokedex()

# ------------------------------------
# SISTEMA PRINCIPAL - AKINATOR POKÉMON
# ------------------------------------

candidatos = pokedex[:]  # Copia de los pokemones disponibles

print("\n¡Piensa en un Pokémon! Voy a intentar adivinarlo.\n")

# Obtener tipos únicos del archivo
tipos_disponibles = obtener_todos_los_tipos(candidatos)

# ---------------------------
# PREGUNTAS POR TIPO
# ---------------------------

# ¿TIENE EVOLUCIÓN?
if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon tiene evoluciones?"):
        candidatos = filtrar_por_evolucion(candidatos, True)
    else:
        candidatos = filtrar_por_evolucion(candidatos, False)

# ¿TIENE MÁS DE UN TIPO?
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

# ¿Puede evolucionar todavía?
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
# ALTURA 
# ---------------------------
if len(candidatos) > 1:
    if preguntar_si_no("¿Mide más de 1 metro?"):
        candidatos = filtrar_por_altura(candidatos, 1.0)
    else:
        candidatos = filtrar_por_altura(candidatos, 0.0, 1.0)

# ---------------------------
# PESO 
# ---------------------------
if len(candidatos) > 1:
    if preguntar_si_no("¿Pesa más de 20 kg?"):
        candidatos = filtrar_por_peso(candidatos, 20.0)
    else:
        candidatos = filtrar_por_peso(candidatos, 0.0, 20.0)

# ---------------------------
# DEBILIDADES
# ---------------------------

if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon es débil a 3 o más tipos?"):
        max_debilidades = 3
    else:
        max_debilidades = 2

debilidades_comunes = ["Fighting", "Electric", "Ice", "Water", "Poison", "Rock", "Psychic", "Fire", "Ground"]

debilidades_encontradas = 0

for debilidad in debilidades_comunes:
    if len(candidatos) <= 1:
        break
    if debilidades_encontradas >= max_debilidades:
        break  # ya se encontraron las necesarias

    if preguntar_si_no(f"¿Tu Pokémon es débil al tipo {debilidad}?"):
        # ANTES: candidatos = es_debil_a(candidatos, debilidad)  (esto estaba mal)
        candidatos = [p for p in candidatos if es_debil_a(p, debilidad)]
        debilidades_encontradas += 1
        
# ---------------------------
# POPULARIDAD
# ---------------------------
if len(candidatos) > 1:
    if preguntar_si_no("¿Tu Pokémon es popular?"):
        candidatos = [p for p in candidatos if es_popular(p)]
    else:
        candidatos = [p for p in candidatos if not es_popular(p)]

# ------------------------------------
# RESULTADO FINAL
# ------------------------------------

import webbrowser

print("\n---------------------------------")
print("Pokémon posibles:", len(candidatos))
print("---------------------------------\n")

if len(candidatos) == 1:
    pokemon = candidatos[0]
    print("¡Creo que tu Pokémon es... 👉 " + pokemon["name"] + "!\n")
    print("Abriendo imagen en el navegador...")
    webbrowser.open(pokemon["img"])

elif len(candidatos) > 1:
    print("No estoy seguro, podrían ser estos:\n")
    for p in candidatos:
        print("-", p["name"])
        webbrowser.open(p["img"])  # 🔥 Abre la imagen de cada uno

else:
    print("No encontré ningún Pokémon con esas características.")