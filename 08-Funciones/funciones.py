"""Conjunto de instrucciones agrupadas bajo un nombre en concreto
pueden reutilizarse invocando a la funcion tantas veces
como sea necesario

def nombre_de_mi_funcion(parametros):
    # BLOQUE DE CODIGO / CONJUNTO DE INSTRUCCIONES

nombre_de_mi_funcion(mi_parametro)
nombre_de_mi_funcion(mi_parametro)
"""

# Ejemplo 1
print("-----------------------------")
print("######### EJEMPLO 1 #########")
print("-----------------------------")
# Definir funcion

def MuestraNombre():
    print("Juan")
    print("David")
    print("Rosas")
    print("Diaz")

# Invocar funcion

MuestraNombre()

# Ejemplo 2: Parametros
print("-----------------------------")
print("######### EJEMPLO 2 #########")
print("-----------------------------")

def  MostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")

"""    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Y no eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))"""

nombre = "Juan David"
edad = 20

MostrarTuNombre(nombre, edad)

"""MostrarTuNombre("Paquito")
MostrarTuNombre("Pepito")"""

# Ejemplo 3 
print("-----------------------------")
print("######### EJEMPLO 3 #########")
print("-----------------------------")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1
print("-----------------------------")
print("######### EJEMPLO 3.1 #########")
print("-----------------------------")

for numero_tabla in range (1, 11):
    tabla(numero_tabla)

# Ejemplo 4 
print("-----------------------------")
print("######### EJEMPLO 4 #########")
print("-----------------------------")

# Parametros opcionales

def getEmpleado(nombre, CC = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if CC != None:
        print(f"CC: {CC}")

getEmpleado("Juan David", "1010009805")

# Ejemplo 5: Return o devolver datos
print("-----------------------------")
print("######### EJEMPLO 5 #########")
print("-----------------------------")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Juan David"))

# Ejemplo 6
print("-----------------------------")
print("######### EJEMPLO 6 #########")
print("-----------------------------")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(5, 5))

# Ejemplo 7
print("-----------------------------")
print("######### EJEMPLO 7 #########")
print("-----------------------------")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellido(apellidos)
    return texto

print(devuelveTodo("Juan David", "Rosas Diaz"))


