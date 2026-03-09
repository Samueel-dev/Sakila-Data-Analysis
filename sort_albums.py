import sqlite3

# 1. Abrimos el túnel a Chinook
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# 2. El superpoder de hoy: ORDER BY
# Pedimos el Título, lo ordenamos ascendente (ASC) y limitamos a 10
query = "SELECT Title FROM albums ORDER BY Title ASC LIMIT 10"
cursor.execute(query)

print("--- 💿 PRIMEROS 10 ÁLBUMES (A-Z) 💿 ---\n")

# 3. Imprimimos los resultados
for album in cursor.fetchall():
    print(f"-> {album[0]}")

connection.close()

