"""
Ejercicio 5. Crear una lista con el contenido de esta tabla:

ACCION      AVENTURA            DEPORTES
GTA         ASSASINS            FIFA 21
COD         PRINCE OF PERSIA    PRO 21
PUBG        CRASH               MOTO GP 21

Mostrar esta informacion ordenada
"""

tabla = [
    {
        "categoria" : "ACCION",
        "juegos": ["GTA", "Call of Duty", "PUBG"]
    },
    {
        "categoria" : "AVENTURA",
        "juegos": ["ASSASINS", "Prince of Persia", "Crash"]
    },
    {
        "categoria" : "DEPORTES",
        "juegos": ["Fifa 21", "PES 21", "Moto GP 21"]
    }    
]

for categoria in tabla:
    print(f"-----------{categoria['categoria']}-----------")
    for juego in categoria['juegos']:
        print(juego)