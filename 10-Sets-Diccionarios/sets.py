"""
SET es un tipo de dato, para tener un coleccion de valores,
pero no tiene ni indice ni orden
"""

personas = {
    "Juan",
    "John",
    "Elsa",
}

personas.add("Manolo")
personas.remove("Juan")

print(type(personas))
print(personas)