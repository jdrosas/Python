"""
Ejercicio 4.
    - Pedir dos numeros al usario y hacer todas las
    operaciones basicas de una calculadora y mostrar
    en pantalla.
"""

print("***********CALCULADORA***************")
numero1 = int(input("Por favor escribe el primer numero: "))
numero2 = int(input("Por favor escribe el segundo numero: "))

print(f"La suma es: {numero1 + numero2}")
print(f"La resta es: {numero1 - numero2}")
print(f"La multiplicacion es: {numero1 * numero2}")
print(f"La division es: {numero1 / numero2}")

print("\n---------------- SOLUCION -------------------")

numero1 = int(input("Por favor escribe el primer numero: "))
numero2 = int(input("Por favor escribe el segundo numero: "))

print("\n***********CALCULADORA***************")
print("Suma: " + str(numero1+numero2))
print("Resta: " + str(numero1-numero2))
print("Multiplicacion: " + str(numero1*numero2))
print("Division " + str(numero1/numero2))