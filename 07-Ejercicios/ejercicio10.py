"""
Ejercicio 10.
    - Hacer un programa que le pida al usuario la nota
    de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos
    han reprobado
"""

contador = 1
aprobados = 0 
reprobados = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno {contador}\"?: "))

    if nota >= 5:
        aprobados += 1
    else:
        reprobados += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")