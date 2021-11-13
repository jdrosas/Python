import os, shutil
from typing import ContextManager

# Crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# Borrar carpeta

"""os.rmdir('./mi_carpeta')"""

# Copiar carpeta

"""ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

shutil.copytree(ruta_original, ruta_nueva)"""

# Listar archivos de carpeta

print("Contenido de mi carpeta:")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for fichero in contenido:
    print("Fichero: " + fichero)