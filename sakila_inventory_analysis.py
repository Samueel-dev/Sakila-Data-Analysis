import sqlite3

def analyze_sakila_inventory():
    # Conexion a la base de datos Sakila
    # (Asegurate de tener el archivo sakila.db en tu carpeta de Termux)
    try:
        db = sqlite3.connect("sakila.db")
        cur = db.cursor()

        print("--- ANALISIS DE INVENTARIO SAKILA (DIA 30) ---")
        print("Obteniendo las categorias con mayor numero de peliculas...\n")

        # SQL: Unimos la tabla de nombres de categoria con la tabla relacional
        query = """
        SELECT 
            c.name AS category_name, 
            COUNT(fc.film_id) AS total_films
        FROM category c
        JOIN film_category fc ON c.category_id = fc.category_id
        GROUP BY c.name
        ORDER BY total_films DESC
        LIMIT 5;
        """

        cur.execute(query)
        results = cur.fetchall()

        # Formateo de tabla profesional
        header = f"{'Categoria':<15} | {'Cantidad de Peliculas':<20}"
        print(header)
        print("-" * len(header))

        for row in results:
            name = row[0]
            count = row[1]
            print(f"{name:<15} | {count:<20}")

    except sqlite3.Error as e:
        print(f"Error al conectar con Sakila: {e}")
    finally:
        if db:
            db.close()

# --- Ejecucion ---
analyze_sakila_inventory()

