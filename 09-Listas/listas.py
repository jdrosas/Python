"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("2pac", "Drake", "Post Malone"))
años = list(range(2020, 2050))
variada = ["Juan David", 30, 10.5, True, "Rosas Diaz"]

"""print(pelicula)
print(peliculas)
print(cantantes)
print(años)
print(variada)"""

# Indices
pelicula = "otra cosa"
peliculas[1] = "Pulp Fiction"
peliculas[2] = "Reservoir Dogs"
print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

# Añadir elementos a lista
cantantes.append("Kase O")
cantantes.append("Residente")
print(cantantes)

# Recorrer lista

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n**********LISTADO DE PELICULAS**********")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")