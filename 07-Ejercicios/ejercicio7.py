"""
Ejercicio 7.
    - Hacer un programa que muestre todos los numeros impares 
    entre dos numeros que decida el usuario.
"""

numero1 = int(input("Escribre el primer numero: "))
numero2 = int(input("Escribre el segundo numero: "))

if numero1 < numero2:

    for x in range (numero1, (numero2 + 1)):
        if x%2 == 0:
           print()
        else:
            print(f"{x} es IMPAR")

else:
    print("El numero 1 debe ser mayor al 2")

    