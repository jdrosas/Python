"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenar y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear la lista
numeros = [77, 64, 23, 56, 43, 21, 10, 98]
# Hacer funcion que recorra listas de numeros y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elementos: " + str(elemento)
        resultado += "\n"

    return resultado

# Recorrer y mostrar
print("########### Recorrer y mostrar ###########")

"""for numero in numeros:
    print(numero)"""

print(mostrarLista(numeros))
print(mostrarLista(numeros))
print(mostrarLista(["Juan", "David"]))

# Ordenar y mostrar
print("########### Ordenar y mostrar ###########")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar Longitud
print("########### Mostrar Longitud ###########")
print(len(numeros))

# Busqueda en la lista
print("########### Busqueda en la lista ###########")

busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"##### BUscar en la lista el numero {busqueda} #####")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el indice: {search}")