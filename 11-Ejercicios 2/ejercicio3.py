"""
Ejercicio 3. Programa que compruebe si una variable esta vacia
y si esta vacia, rellanarla con texto en minusculas y mostrarlo
en mayusculas.
"""

texto = ""

if len(texto.strip()) <= 0:

    texto = "hola soy un texto"
    print(texto.upper())

else:
    print(f"La variable tiene contenido {texto}")