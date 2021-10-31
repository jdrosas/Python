cantantes = ['2pac', 'Biggie', 'Snoop']
numeros = [1, 9, 2, 3, 8, 4, 5, 6, 7]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Easy E")
cantantes.insert(2, "Ice Cube")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove('Snoop')
print(cantantes)

# Dar vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('2pac' in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("2pac"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)