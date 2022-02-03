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
    print("Ok!! Vamos a registrarte en el sistema")

elif accion == "Login":
    print("Vale!! Identificate en el sistema")
