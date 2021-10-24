"""
Variables locales: Se definen dentro de la funcion y no 
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un retur

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas.
"""

# Variables globales
frase = "No sé, cualquier cosa."

print(frase)

def holaMundo():
    frase = "Hola Mundo!" # Variable local
    print("Dentro de la funcion")
    print(frase)

    year = 2021 # Variable local
    print(year)

    global website # Convertir a variable global
    website = "google.com"
    print(website)

holaMundo()
print(website)

