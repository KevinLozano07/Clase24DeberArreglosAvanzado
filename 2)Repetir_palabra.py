#Crea un arreglo con una lista de palabras. Luego, cuenta cuántas veces aparece una palabra específica en el arreglo y muestra el resultado.

Elementos = ["Agua", "Tierra", "Fuego", "Agua", "Aire", "Fuego", "Agua", "Tierra", "Agua", "Tierra", "Aire", "Agua", "Agua", "Tierra", "Tierra", "Agua", "Fuego", "Aire", "Agua"]

Palabra = "Agua"

Contador = 0

for El in Elementos:
    if El == Palabra:
        Contador += 1

print("")
print(f"La palabra {Palabra} aparece un total de: {Contador} veces")
print("")