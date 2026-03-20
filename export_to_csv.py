import sqlite3
import csv

# 1. Connection
db = sqlite3.connect("chinook.db")
cur = db.cursor()

print("--- 📊 EXPORTING SALES REPORT TO CSV ---")

# 2. SQL Query: Sales per Genre
query = """
SELECT g.Name, SUM(ii.UnitPrice * ii.Quantity) as TotalSales
FROM genres g
JOIN tracks t ON g.GenreId = t.GenreId
JOIN invoice_items ii ON t.TrackId = ii.TrackId
GROUP BY g.Name
ORDER BY TotalSales DESC;
"""

cur.execute(query)
results = cur.fetchall()

# 3. Save to CSV file
with open('genre_sales_report.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Genre', 'Total_Sales_USD'])
    # Write data
    writer.writerows(results)

print("📂 Report saved as 'genre_sales_report.csv'!")
db.close()

