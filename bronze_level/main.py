import os

from persistence.login_db_service import login_database
from persistence.persistence_line_db import persistence_line_db
from persistence.read_csv import read_fraud_file

if __name__ == "__main__":
    file_path = os.path.join('data', 'synthetic_fraud_data.csv')
    conn = login_database()
    for line in read_fraud_file(file_path):
        persistence_line_db(conn, line)
