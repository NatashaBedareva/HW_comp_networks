import os
import csv
import json

from app import run_parsing

from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv, dotenv_values


app = Flask(__name__)

def data_to_SQL(csv_file_path):
    load_dotenv()

    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    db_name = os.getenv("DB_NAME")
    table_name = os.getenv("TABLE_NAME")
    port = os.getenv("PORT")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    data = pd.read_csv(csv_file_path)
    data.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data {csv_file_path} write to tabel {table_name} in BD {db_name}.")


@app.route('/')
def run_app():
    out = "out.csv"
    run_parsing(out)
    data_to_SQL(out)
    return make_json(out)

def make_json(csvFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['product_name']
            data[key] = rows

    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
