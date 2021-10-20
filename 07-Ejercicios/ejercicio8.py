"""
Ejercicio 8.
    - ¿CUanto es el X por ciento de X numero?
    20 % de 150
"""

numero1 = int(input("Escribe el nuemero: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {numero1}?: "))
operacion = (numero1 * (porcentaje/100))

print(f"El {porcentaje}% de {numero1} es: {operacion}")
