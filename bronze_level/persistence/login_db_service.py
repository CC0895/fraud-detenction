import os
import logging
import psycopg2
from psycopg2.extras import LoggingConnection

def login_database():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    db_settings = {
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "host": "fraud_analysis_integration",
        "database": os.getenv("INTEGRATION_DB"),
    }

    try:
        conn = psycopg2.connect(connection_factory=LoggingConnection, **db_settings)
        conn.initialize(logger)
        logger.info("Connessione al database riuscita!")

        return conn

    except Exception as e:
        logger.error(f"Errore durante la connessione al database: {e}")
        return None


