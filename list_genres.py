import sqlite3

# 1. Abrimos el túnel a Chinook
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# 2. La consulta más sencilla del mundo
# Solo queremos los nombres de la tabla 'genres'
cursor.execute("SELECT Name FROM genres")

print("--- GÉNEROS MUSICALES EN CHINOOK ---\n")

# 3. Imprimimos los resultados
for genero in cursor.fetchall():
    print(f"-> {genero[0]}")

connection.close()
