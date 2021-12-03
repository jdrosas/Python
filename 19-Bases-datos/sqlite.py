# Importar modulo

import sqlite3

# Conexion 
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id integer primary key autoincrement,"+
"titulo varchar(255), "+
"descripcion TEXT, "+
"precio int(255)"+
")")

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("Nombre:", producto[1])
    print("Descripcion:", producto[2])
    print("Descripcion:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

# Cerar conexion
conexion.close()