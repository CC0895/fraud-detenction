def read_data(conn, batch_id,  chunk_size=100):
    curr = conn.cursor()
    query = """SELECT 
    merchant_category, 
    merchant_type,
    merchant 
    FROM fraud_transaction where batch_id = %s"""

    curr.execute(query, (batch_id,))

    while True:
        rows = curr.fetchmany(chunk_size)
        if not rows:
            break
        for row in rows:
            yield row