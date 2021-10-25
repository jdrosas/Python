nombre = "Juan David"

# Funciones generales
print(nombre)

# Detectar el tipado
comprobador = isinstance(nombre, str)
if comprobador:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = "    mi contenido     "
print(frase)
print(frase.strip())

# Eliminar variables 
year = 2021
print(year)
del year
# print(year)

# Comprobar variable vacia
texto = "  ff  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ",len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

# Remplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())