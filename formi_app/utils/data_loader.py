import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def load_csv_to_dict(filename):
    data = []
    file_path = os.path.join(DATA_DIR, filename)
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data

def load_all_data():
    return {
        "rooms": load_csv_to_dict("rooms_cleaned.csv"),
        "rules": load_csv_to_dict("rules_cleaned.csv"),
        "queries": load_csv_to_dict("queries_cleaned.csv"),
        "pricing": load_csv_to_dict("pricing_cleaned.csv")
    }
