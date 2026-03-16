import sqlite3

# 1. Connect to the database
db = sqlite3.connect("chinook.db")
cur = db.cursor()

# 2. Target ID to delete (Let's assume ArtistId 276 is a test)
target_id = 276 

print(f"--- DATABASE CLEANUP ---")

# 3. SQL DELETE with WHERE (Crucial for safety!)
query = "DELETE FROM artists WHERE ArtistId = ?"

try:
    cur.execute(query, (target_id,))
    # 4. COMMIT is required to save deletions!
    db.commit()
    print(f"Successfully deleted artist with ID: {target_id}")
except Exception as e:
    print(f"An error occurred: {e}")

# 5. Close
db.close()

