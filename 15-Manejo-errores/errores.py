# Capturar excepciones y manejar errores en codigo
# susceptible a fallos/errores

"""try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, el nombre no cumple con las caracteristicas")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteración!!")
"""
# Busqueda en la lista

"""try:
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
except:
    print("El numero no esta en la lista")
"""

# Manejar multiples excepciones

"""try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas antes a enteros!!")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""

# Excepciones personalizadas o lanzar excepcion

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvido {nombre}")
except ValueError:
    print("Introduce los datos correctamente")    
except Exception as e:
    print("Existe un error: ", e)