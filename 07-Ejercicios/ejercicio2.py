"""
Ejercicio 2.
    - Escribir un script que nos muestre por pantalla
    todos los numeros pares del 1 al 120
"""

contador = 2
muestrame = str(0)

while contador <= 120:
    muestrame = muestrame + " , " + str(contador)
    contador = contador + 2

print(muestrame)

print("---------------- SOLUCION -------------------")

contador = 1

for contador in range (1, 121):
    if contador%2 == 0:
        print(contador)