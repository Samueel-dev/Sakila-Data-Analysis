"""
Inventory Price Updater
Author: Samueel-dev
Description: Script to update game prices in the database.
"""
import sqlite3

# Establish connection
connection = sqlite3.connect("store.db")
cursor = connection.cursor()

print("--- Game Inventory Update System ---")

# 1. Ask for the game name (using your new keys!)
target_game = input("\nEnter the name of the game to update: ").lower()

# 2. Ask for the new price
try:
    new_price = float(input("Enter the new price: "))
    
    # 3. SQL UPDATE Logic
    # We use LIKE to be flexible with the name
    query = "UPDATE games SET price = ? WHERE LOWER(title) LIKE ?"
    cursor.execute(query, (new_price, f"%{target_game}%"))
    
    # 4. Save the changes (CRITICAL STEP)
    connection.commit()
    
    # Check if the update actually happened
    if cursor.rowcount > 0:
        print(f"\n[SUCCESS] Updated {cursor.rowcount} record(s).")
    else:
        print("\n[ERROR] Game not found. No changes applied.")

except ValueError:
    print("\n[ERROR] Please enter a valid number for the price.")

# Show updated table
print("\n--- Updated Inventory ---")
cursor.execute("SELECT * FROM games ORDER BY price DESC")
for game in cursor.fetchall():
    print(f"ID: {game[0]} | Title: {game[1]:<15} | Price: ${game[2]}")

connection.close() 
