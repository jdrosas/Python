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

*********************************************

# Operadores logicos

and: Y
or: O
!: NEGACION
not: NO

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


# Ejemplo 4
print("\n################ EJEMPLO 4 ###############")

dia = 1 
"""int(input("Introduce el numero del dai de la semana: "))"""

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print("Es sabado")
                    else:
                        if dia == 7:
                            print("Es domingo")"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print ("Es martes")
elif dia == 3:
    print ("Es miercoles")
elif dia == 4:
    print ("Es jueves")
elif dia == 5:
    print ("Es viernes")
elif dia == 6:
    print ("Es sabado")
elif dia == 7:
    print ("Es domingo")

# Ejemplo 5
print("\n################ EJEMPLO 5 ###############")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("Introduce tu edad: "))
edad_oficial = 20

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n################ EJEMPLO 6 ###############")

pais = "Italia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

# Ejemplo 7
print("\n################ EJEMPLO 7 ###############")

pais = "Mexico"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")

# Ejemplo 8
print("\n################ EJEMPLO 8 ###############")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")
