from datos import cargar_pokedex, tipo

pokedex = cargar_pokedex()

print("Total de Pokémon cargados:", len(pokedex))
print(pokedex[0])
print("Primer Pokémon:", pokedex[0]["name"])
print("Tipos:", pokedex[0]["type"])

for pokemon in pokedex[:5]:
    if tipo(pokemon, "Water"):
        print(pokemon["name"], "es de tipo Agua")
    else:
        print(pokemon["name"], "NO es de tipo Agua")
