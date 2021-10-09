"""
# FOR

for variable in elemento iterable (lista, rango, etc)
    bloque de instrucciones

"""
contador = 0
resultado = 0

for contador in range (0, 5):
    print("Voy por el " + str(contador))

    resultado = resultado + contador

print(f"El resulado es : {resultado}")

# Ejemplo tablas de multiplicar
print("\n************** EJEMPLO ***************")

numero_usuario = int(input("De que numero deseas ver la tabla: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### TABLA DE MULTIPLICAR DEL NUMERO {numero_usuario} ###")

for numero_tabla in range(1, 11):

    if numero_usuario >= 10:
        print("Este numero no es valido")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("### FIN TABLA ###")


