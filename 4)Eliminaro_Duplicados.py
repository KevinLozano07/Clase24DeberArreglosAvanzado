#Crea un arreglo con palabras que incluyan algunas duplicadas. Luego, elimina las palabras duplicadas y muestra el resultado.

Palabras = ["Dia", "Noche", "Noche", "Noche", "Dia", "Noche", "Dia", "Dia", "Noche", "Noche", "Noche", "Dia", "Noche"]

Palabras_sin_duplicar = []

for Palabra in Palabras:
    if Palabra not in Palabras_sin_duplicar:
        Palabras_sin_duplicar.append(Palabra)

print("")
print(f"Arreglo sin palabras duplicadas: {Palabras_sin_duplicar}")
print("")