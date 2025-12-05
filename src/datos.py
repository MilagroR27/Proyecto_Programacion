import json  # Importa el módulo para trabajar con archivos JSON

def cargar_pokedex():
# Abre el archivo 'pokemon.json' ubicado dentro de la carpeta 'data' en modo lectura ("r")
# encoding="utf-8" asegura que se lean correctamente caracteres especiales como tildes o ñ
    with open("./data/pokemon.json", "r", encoding="utf-8") as archivo:    
# Convierte el contenido del archivo JSON a estructuras de Python (listas y diccionarios)
        data = json.load(archivo)
# Del diccionario principal, devuelve solo la lista de pokémon asociada a la clave "pokemon"
    return data["pokemon"]
