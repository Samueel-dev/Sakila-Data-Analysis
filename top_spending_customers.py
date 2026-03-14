import sqlite3

# 1. Connection
db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 🏆 CHINOOK TOP SPENDERS ---")

# 2. SQL: Sum total by CustomerId and sort
query = """
SELECT CustomerId, SUM(Total) 
FROM invoices 
GROUP BY CustomerId 
ORDER BY SUM(Total) DESC 
LIMIT 5
"""
cur.execute(query)

# 3. Show Top 5
for row in cur.fetchall():
    print(f"Customer ID: {row[0]} | Total Spent: ${row[1]:.2f}")

db.close()

