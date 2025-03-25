from datetime import datetime

def persistence_merchant_db(conn, tupla):
    curr = conn.cursor()
    now = datetime.now()
    query = """INSERT INTO merchant (
        merchant_category, 
        merchant_type,
        merchant,
        update_time
    ) VALUES (
        %s, %s, %s, %s
    )
    ON CONFLICT (merchant_category, merchant_type, merchant) 
    DO UPDATE SET
        merchant_category = excluded.merchant_category,
        merchant_type = excluded.merchant_type,
        merchant = excluded.merchant,
        update_time = EXCLUDED.update_time
    """

    try:
        curr.execute(query, tupla + (now,))
        conn.commit()
        print("Inserimento completato con successo.")
    except Exception as e:
        conn.rollback()
        print(f"Errore durante l'inserimento: {e}")
    finally:
        curr.close()
