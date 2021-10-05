"""Variable: contenedor de infomarción que dentro
guardará un dato, se pueden crear muchas variables
y que cada una tenga un dato distinto"""

#Crear variables y asignar un valor
texto = "Juan David"
texto2 = "Rosas Diaz"
numero = 45
decimal = 7.1

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("-------------------------------")

#Sustituir datos en variables / reasignar valores
numero = 15
decimal = 15.1
print(numero)
print(decimal)

print("-------------------------------")

#Concatenación
nombres = "Juan David"
apellidos = "Rosas Diaz"
ciudad = "Bogotá"

print(nombres + " " + apellidos + " - " + ciudad)
print(f"{nombres} {apellidos} - {ciudad}")
print("Hola mi nombre es {} {} y soy de la ciudad de {}".format(nombres, apellidos, ciudad))
print(nombres, apellidos, ciudad)
print("-------------------------------")