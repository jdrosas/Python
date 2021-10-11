"""
Ejercicio 3.
    - Escribir un programa que muestre los cuadrados 
    (un numero multiplicado por si mismo) de los primeros numeros 60
    naturales. Usando el ciclo for y el ciclo while.
"""

print("\n----------------- CICLO FOR -----------------")

# Ciclo FOR 

numero = 0
cuadrado = 0

for numero in range(0, 60):

    numero = numero + 1
    cuadrado = numero * numero

    print(f"El cuadrado de " + str(numero) + " " + "es = " + str(cuadrado))

print("\n----------------- CICLO WHILE -----------------")
# Ciclo While

numero = 0
cuadrado = 0

while numero <= 59:
    
    numero = numero + 1
    cuadrado = numero * numero

    print(f"El cuadrado de " + str(numero) + " " + "es = " + str(cuadrado))

print("\n---------------- SOLUCION -------------------")

print("\n----------------- CICLO FOR -----------------")
# Ciclo For

for numero in range(61):
    cuadrado = numero*numero
    print(f"EL cuadrado de {numero} es {cuadrado}")


print("\n----------------- CICLO WHILE -----------------")

# Ciclo While

contador = 0

while contador <= 60:

    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")

    contador += 1



