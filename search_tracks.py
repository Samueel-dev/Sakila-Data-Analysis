import sqlite3

# 1. Conexión
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# 2. Entrada del usuario
search = input("¿Qué canción buscas? ")

# 3. SQL con FILTRO (WHERE y LIKE)
# El símbolo % sirve para buscar la palabra en cualquier parte del título
query = "SELECT Name FROM tracks WHERE Name LIKE ?"
cursor.execute(query, (f"%{search}%",))

print(f"\n--- 🔎 RESULTADOS PARA: '{search}' ---\n")

# 4. Mostrar resultados
results = cursor.fetchall()

if results:
    for row in results:
        print(f"🎵 {row[0]}")
else:
    print("No se encontraron canciones con ese nombre.")

connection.close()
