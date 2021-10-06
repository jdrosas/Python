"""
# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

*********************************************

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de comparación
== Igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

"""

# Ejemplo 1
print("\n################ EJEMPLO 1 ###############")

color = "rojo"
#color = input("Adivina el color: ")

if color == "rojo":
    print("ENHORABUENA!!")
    print("El color es rojo")
else:
    print("El color es incorrecto")


# Ejemplo 2
print("\n################ EJEMPLO 2 ###############")

year = 2020
#year = int(input("¿En que año estamos?: "))

if year >= 2021: 
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")


# Ejemplo 3
print("\n################ EJEMPLO 3 ###############")

nombre = "Juan David"
ciudad = "Bogotá"
pais = "Colombia"
edad = 20
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if pais != "Colombia":
        print("El usuario no es Colombiano")
    else:
        print(f"Es Colombiano y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")
