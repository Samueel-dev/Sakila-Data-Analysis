# -*- coding: utf-8 -*-
import sqlite3  # Importamos la librería para manejar la base de datos

# Connect to the Sakila database
connection = sqlite3.connect("sakila.db")
cursor = connection.cursor()

# Query: Get the top 5 actors with the most films
# We use INNER JOIN to connect actors with their filmography through the bridge table
query = '''
SELECT actor.first_name, actor.last_name,
       COUNT(film_actor.film_id) AS total_films
FROM actor 
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
GROUP BY actor.actor_id
ORDER BY total_films DESC
LIMIT 5;
'''

cursor.execute(query)
actor_info = cursor.fetchall()

print("--- Sakila Top Actors Report ---\n")

# Display results with professional formatting
for a in actor_info:
    full_name = f"{a[0]} {a[1]}"
    total_films = a[2]
    # We use :<25 to align the text to the left and create a clean column
    print(f"Actor: {full_name:<25} | Total Films: {total_films}")
    
connection.close()
