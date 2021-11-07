"""
Modulos: son funcionalidades ya hechas para reutilizar.
En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y tambien podemos crear nuestros modulos
"""

# Importar modulo propio
# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Juan David"))
#print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Juan David"))
print(calculadora(5, 4, True))

# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().time())