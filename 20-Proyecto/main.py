"""
Proyecto Python y MySql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas
"""


print("""
-------------------------------------------------------------------------
Acciones disponibles:

    - Registro
    - Login

-------------------------------------------------------------------------
""")

accion = input("¿Que quieres hacer?: ")

if accion == "Registro":
    print("\nOk!! Vamos a registrarte en el sistema")
    nombre = input("¿Cual es tu nombre?: ")
    apellido = input("¿Cuales son tus apellidos?: ")
    email = input("¿Introduce tu correo electronico?: ")
    password = input("¿Introduce tu contraseña?: ")

elif accion == "Login":
    print("\nVale!! Identificate en el sistema")
    email = input("¿Introduce tu correo electronico?: ")
    password = input("¿Introduce tu contraseña?: ")