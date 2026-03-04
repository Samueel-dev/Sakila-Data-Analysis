import sqlite3

# 1. Nos conectamos a Chinook
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# 2. Pedimos SOLO la columna 'Name' que descubriste, y limitamos a 10
query = "SELECT Name FROM artists LIMIT 10"
cursor.execute(query)

print("--- Primeros 10 Artistas en Chinook ---\n")

# 3. Imprimimos los resultados
for artista in cursor.fetchall():
    print(f"- {artista[0]}")

# 4. Cerramos
connection.close() 
