import sqlite3

def generate_monthly_report():
    # Conexion a la base de datos Chinook
    db = sqlite3.connect("chinook.db")
    cur = db.cursor()

    print("--- REPORTE MENSUAL DE VENTAS ---")
    print("Analizando tendencia de ingresos por mes...\n")

    # SQL: strftime('%Y-%m', ...) extrae el Año y el Mes
    query = """
    SELECT 
        strftime('%Y-%m', InvoiceDate) AS Month, 
        SUM(Total) AS Monthly_Total,
        COUNT(InvoiceId) AS Transactions
    FROM invoices
    GROUP BY Month
    ORDER BY Month ASC
    LIMIT 12;
    """

    try:
        cur.execute(query)
        results = cur.fetchall()

        # Cabecera del reporte
        header = f"{'Mes':<10} | {'Ventas':<12} | {'Transacciones':<15}"
        print(header)
        print("-" * len(header))

        for row in results:
            month = row[0]
            total = round(row[1], 2)
            transactions = row[2]
            print(f"{month:<10} | ${total:<11} | {transactions:<15}")

    except sqlite3.Error as e:
        print(f"Error al procesar fechas: {e}")
    finally:
        db.close()

# --- Ejecucion ---
generate_monthly_report()

