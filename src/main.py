from datos import cargar_pokedex

pokedex = cargar_pokedex()

print("Total de Pokémon cargados:", len(pokedex))
print("Primer Pokémon:", pokedex[0]["name"])
print("Tipos:", pokedex[0]["type"])
