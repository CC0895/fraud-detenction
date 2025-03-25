from persistence.login_db_service import DatabaseConnector
from persistence.merchant.read_merchant import read_data
from persistence.merchant.persistence_merchant import persistence_merchant_db
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        batch_id = sys.argv[1]
        db_connector = DatabaseConnector()
        integration_connection = db_connector.connect("fraud_analysis_integration")
        transformation_connection = db_connector.connect("fraud_analysis_transformation")
        merchant = read_data(integration_connection, batch_id),
        persistence_merchant_db(transformation_connection, merchant)
        db_connector.close_connection()
    else:
        print("Errore: Nessun batch_id fornito.")
        sys.exit(1)

