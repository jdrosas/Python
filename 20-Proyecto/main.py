"""
Proyecto Python y MySql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas
"""

from usuarios import acciones

print("""
-------------------------------------------------------------------------
Acciones disponibles:

    - Registro
    - Login

-------------------------------------------------------------------------
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "Registro":
    hazEl.Registro()

elif accion == "Login":
    hazEl.Login()
