"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En un formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Juan David",
    "apellidos": "Rosas",
    "web": "jrosas.com"
}

print(persona["apellidos"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Juan David',
        'email': 'jrosas@jrosas.com'
    },
    {
        'nombre': 'Elsa',
        'email': 'ediaz@ediaz.com'
    },
    {
        'nombre': 'John',
        'email': 'jjrosas@jjrosas.com'
    }
]

print(contactos[1]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------")