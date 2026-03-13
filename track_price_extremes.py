import sqlite3

# 1. Open connection to Chinook database
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

print("--- 💸 CHINOOK PRICING ANALYSIS ---")

# 2. SQL Magic: Finding Max and Min prices
# We select both values in a single query
query = "SELECT MAX(UnitPrice), MIN(UnitPrice) FROM tracks"
cursor.execute(query)

# 3. Fetch results
max_price, min_price = cursor.fetchone()

print(f"The most expensive track costs: ${max_price}")
print(f"The cheapest track costs: ${min_price}")

# 4. Close the tunnel
connection.close()

