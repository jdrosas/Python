from io import open
import pathlib 
import shutil
import os
import os.path

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

# Copiar
"""ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-Ejercicios/fichero_copiado_desde_14.txt"

shutil.copyfile(ruta_original, ruta_alternativa)"""

# Mover

"""ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"

shutil.move(ruta_original, ruta_nueva)>"""

# Eliminar

"""ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"
os.remove(ruta_nueva)
"""
# Comprobar si existe

"""Esto es igual
os.path.abspath("./") == str(pathlib.Path().absolute()) """

"""print(os.path.abspath("./"))"""

ruta_comprobar = os.path.abspath("./") + "/fichero_texto55.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
