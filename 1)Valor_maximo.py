#Crea un arreglo con 7 números de tu elección y escribe un código que encuentre y muestre el valor mínimo.

Numeros = [965, 395, 100, 215, 232, 777, 9]

Max = Numeros[0]

for Num in Numeros:
    if Num > Max:
        Max = Num

print("")
print("El valor maximo es:", Max)
print("")