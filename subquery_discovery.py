import sqlite3

db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 🔍 SQL SUBQUERY: TRACKS BY ARTIST NAME ---")

# La magia: El SELECT interno encuentra el ID, el externo trae las canciones
query = """
SELECT Name, Composer 
FROM tracks 
WHERE AlbumId IN (
    SELECT AlbumId FROM albums WHERE ArtistId = (
        SELECT ArtistId FROM artists WHERE Name = 'Queen'
    )
)
LIMIT 10;
"""

cur.execute(query)
results = cur.fetchall()

for row in results:
    print(f"🎵 Song: {row[0]} | ✍️ Composer: {row[1]}")

db.close()

