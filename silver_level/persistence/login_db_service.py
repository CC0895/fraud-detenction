import os
import logging
import psycopg2
from psycopg2.extras import LoggingConnection

class DatabaseConnector:
    def __init__(self):
        self.logger = self._setup_logger()
        self.conn = None

    def _setup_logger(self):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(self.__class__.__name__)
        return logger

    def connect(self, host):
        db_settings = {
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD"),
            "host": host,
            "database": os.getenv("POSTGRES_DB"),
        }

        try:
            self.conn = psycopg2.connect(connection_factory=LoggingConnection, **db_settings)
            self.conn.initialize(self.logger)
            self.logger.info("Connessione al database riuscita!")
            return self.conn

        except Exception as e:
            self.logger.error(f"Errore durante la connessione al database: {e}")
            return None

    def close_connection(self):
        if self.conn:
            try:
                self.conn.close()
                self.logger.info("Connessione al database chiusa con successo.")
            except Exception as e:
                self.logger.error(f"Errore durante la chiusura della connessione: {e}")


