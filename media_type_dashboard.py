import sqlite3

db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 📈 MEDIA TYPE DISTRIBUTION (ASCII CHART) ---")

query = """
SELECT mt.Name, COUNT(t.TrackId) as Total
FROM media_types mt
JOIN tracks t ON mt.MediaTypeId = t.MediaTypeId
GROUP BY mt.Name;
"""

cur.execute(query)
rows = cur.fetchall()

# Dibujamos la gráfica
for name, total in rows:
    # Creamos una barra: 1 '#' por cada 100 canciones (escalado)
    bar = "█" * (total // 100) 
    print(f"{name.ljust(25)} | {bar} ({total})")

db.close()

