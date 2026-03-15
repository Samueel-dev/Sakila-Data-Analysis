import sqlite3

# 1. Connect
db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 🎶 ALBUM DETAILS (ARTIST + ALBUM) ---")

# 2. SQL JOIN: Unimos la tabla albums con artists
query = """
SELECT albums.Title, artists.Name
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId
LIMIT 10
"""
cur.execute(query)

# 3. Print
for row in cur.fetchall():
    print(f"Album: {row[0]:<30} | Artist: {row[1]}")

db.close()

