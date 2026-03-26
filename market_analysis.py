import sqlite3

def analyze_high_value_markets(threshold):
    # Conexion a la base de datos Chinook
    db = sqlite3.connect("chinook.db")
    cur = db.cursor()

    print("--- REPORTE DE MERCADOS DE ALTO VALOR ---")
    print(f"Filtrando paises con promedio de venta mayor a: ${threshold}\n")

    # SQL: Usamos AVG para el promedio y HAVING para filtrar el grupo
    query = """
    SELECT 
        BillingCountry, 
        COUNT(InvoiceId) AS Total_Invoices,
        AVG(Total) AS Average_Spent
    FROM invoices
    GROUP BY BillingCountry
    HAVING AVG(Total) > ?
    ORDER BY Average_Spent DESC;
    """

    try:
        cur.execute(query, (threshold,))
        results = cur.fetchall()

        # Formateo de salida en terminal
        header = f"{'Pais':<15} | {'Facturas':<10} | {'Promedio':<10}"
        print(header)
        print("-" * len(header))

        for row in results:
            country = row[0]
            count = row[1]
            avg = round(row[2], 2)
            print(f"{country:<15} | {count:<10} | ${avg:<10}")

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        db.close()

# --- Ejecucion ---
# Buscamos paises donde el promedio de factura sea mayor a 5.50 dolares
analyze_high_value_markets(5.50)

