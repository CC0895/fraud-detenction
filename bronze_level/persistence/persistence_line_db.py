import psycopg2


def persistence_line_db(conn, tupla):
    curr = conn.cursor()

    query = """INSERT INTO fraud_transaction (
        batch_id,
        processed_time,
        transaction_id,
        customer_id,
        card_number,
        timestamp,
        merchant_category,
        merchant_type,
        merchant,
        amount,
        currency,
        country,
        city,
        city_size,
        card_type,
        card_present,
        device,
        channel,
        device_fingerprint,
        ip_address,
        distance_from_home,
        high_risk_merchant,
        transaction_hour,
        weekend_transaction,
        velocity_last_hour,
        is_fraud
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s
    )"""

    try:
        curr.execute(query, tupla)
        conn.commit()
        print("Inserimento completato con successo.")
    except Exception as e:
        conn.rollback()
        print(f"Errore durante l'inserimento: {e}")
    finally:
        curr.close()




