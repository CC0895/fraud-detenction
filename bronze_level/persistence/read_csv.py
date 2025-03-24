import uuid
from datetime import datetime
import csv


def read_fraud_file(path, max_rows=100):
    batch_id = str(uuid.uuid4())
    processed_time = datetime.now()
    count = 0

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            print("row number: ", count)
            raw_line = (batch_id, processed_time, *row)
            yield raw_line


