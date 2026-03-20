import sqlite3

# 1. Connection
db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- CREATING SQL VIEW: MASTER_TRACK_LIST ---")

# 2. SQL: Create a View that joins 3 tables
# This saves the logic inside the database file!
query = """
CREATE VIEW IF NOT EXISTS master_track_list AS
SELECT 
    art.Name AS Artist, 
    alb.Title AS Album, 
    tra.Name AS Track
FROM artists art
JOIN albums alb ON art.ArtistId = alb.ArtistId
JOIN tracks tra ON alb.AlbumId = tra.AlbumId;
"""

try:
    cur.execute(query)
    db.commit()
    print("✅ View created successfully!")
    
    # Let's test the view
    cur.execute("SELECT * FROM master_track_list LIMIT 5")
    for row in cur.fetchall():
        print(f"Artist: {row[0]} | Track: {row[2]}")
        
except Exception as e:
    print(f"Error: {e}")

db.close()
