import sqlite3

def find_unsold_items():
    # Conexion a la base de datos Chinook
    db = sqlite3.connect("chinook.db")
    cur = db.cursor()

    print("--- REPORTE DE PRODUCTOS SIN VENTAS ---")
    print("Buscando tracks que nunca han sido comprados...\n")

    # SQL: LEFT JOIN trae TODO de tracks. 
    # Si no hay coincidencia en invoice_items, esa columna sera NULL.
    query = """
    SELECT t.Name, t.Composer
    FROM tracks t
    LEFT JOIN invoice_items ii ON t.TrackId = ii.TrackId
    WHERE ii.TrackId IS NULL
    LIMIT 15;
    """

    try:
        cur.execute(query)
        results = cur.fetchall()

        if not results:
            print("No se encontraron productos sin vender.")
        else:
            print(f"{'Cancion':<35} | {'Compositor'}")
            print("-" * 60)
            for row in results:
                name = row[0][:30] # Recortamos si el nombre es muy largo
                composer = row[1] if row[1] else "Anonimo"
                print(f"{name:<35} | {composer}")

    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")
    finally:
        db.close()

# --- Ejecucion ---
find_unsold_items()
