from persistence.login_db_service import DatabaseConnector

if __name__ == "__main__":
    db_connector = DatabaseConnector()
    connection = db_connector.connect()
    db_connector.close_connection()
