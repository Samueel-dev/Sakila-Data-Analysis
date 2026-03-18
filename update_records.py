import sqlite3

# 1. Connect
db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 📝 DATABASE UPDATE ---")

# 2. SQL UPDATE: Let's change the name of ArtistId 1
# (Usually 'AC/DC', let's pretend they rebranded to 'AC/DC Legacy')
new_name = "AC/DC Legacy"
artist_id = 1

query = "UPDATE artists SET Name = ? WHERE ArtistId = ?"

try:
    cur.execute(query, (new_name, artist_id))
    # CRITICAL: Always commit when changing data!
    db.commit()
    print(f"Artist {artist_id} updated to: {new_name}")
except Exception as e:
    print(f"Error: {e}")

db.close()

