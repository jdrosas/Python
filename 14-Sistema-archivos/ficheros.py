from io import open
import pathlib 

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir
archivo.write("*********SOY UN TEXTO DESDE PYTHON********\n")

# Cerar
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)
# for elemento in contenido:
#     print(elemento)

# Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close

for frase in lista:

    # lista_frase = frase.split()
    # print(lista_frase)
    print("- "+frase.center(100))