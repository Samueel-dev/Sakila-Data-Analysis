import sqlite3

# 1. Connection (keeping it short for touch typing)
db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 🔥 CHINOOK BEST-SELLING TRACKS ---")

# 2. SQL: Count occurrences of each TrackId
query = """
SELECT TrackId, COUNT(TrackId) 
FROM invoice_items 
GROUP BY TrackId 
ORDER BY COUNT(TrackId) DESC 
LIMIT 10
"""
cur.execute(query)

# 3. Show Results
print("Track ID | Times Sold")
print("--------------------")
for row in cur.fetchall():
    print(f"ID: {row[0]}   | Sales: {row[1]}")

db.close()

