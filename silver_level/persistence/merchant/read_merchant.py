def read_data(conn, batch_id):
    curr = conn.cursor()
    query = """SELECT 
        merchant_category, 
        merchant_type,
        merchant 
        FROM fraud_transaction 
        WHERE batch_id = %s"""

    curr.execute(query, (batch_id,))

    rows = curr.fetchall()  # Usa fetchall() per recuperare tutti i dati in una volta

    return rows  # Restituisci direttamente le righe, una lista di tuple
