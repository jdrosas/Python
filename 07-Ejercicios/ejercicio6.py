"""
Ejercicio 6.
    - Mostrar todas las tablas de multiplicar del 1 al 10.
    Mostrando el titulo de la tabla y luego las multiplicacione del 1 al 10
"""

print("------------TABLAS DE MULTIPLICAR------------")

for cabecera in range(1, 11):
    print("######################")
    print(f"Tabla del {cabecera}")
    

    for numero in range(1, 11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")
    print("######################")
    
    print("\n")