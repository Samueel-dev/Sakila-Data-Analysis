import sqlite3

# 1. Conexión a la base de datos
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# 2. SQL: Usamos COUNT para saber cuántas filas hay en la tabla 'tracks'
query = "SELECT COUNT(*) FROM tracks"
cursor.execute(query)

# 3. Guardamos el resultado (fetch datos)
total = cursor.fetchone()[0]

print(f"--- TOTAL DE CANCIONES EN LA TIENDA ---")
print(f"La base de datos tiene {total} canciones registradas.")

connection.close()
