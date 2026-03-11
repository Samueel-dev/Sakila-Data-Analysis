import sqlite3

# 1. Establish connection to the database
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

print("--- ⏱️ CHINOOK TRACK ANALYTICS ---")

# 2. SQL Query using AVG() function
# Milliseconds is the column name in the 'tracks' table
query = "SELECT AVG(Milliseconds) FROM tracks"
cursor.execute(query)

# 3. Fetch the result
average_ms = cursor.fetchone()[0]

# 4. Convert milliseconds to minutes (1 min = 60,000 ms)
average_min = average_ms / 60000

print(f"The average track duration is: {average_min:.2f} minutes.")

# 5. Close connection
connection.close()
