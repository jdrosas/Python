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

# Cerar conexion
conexion.close()