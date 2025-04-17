from flask import Flask
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')

DATABASE_URI = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'
engine = create_engine(DATABASE_URI)


def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS numbers (
                id SERIAL PRIMARY KEY,
                value INTEGER NOT NULL
            );
        """))


@app.route('/')
def add_db():
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO numbers (value) 
            VALUES (COALESCE((SELECT MAX(value) FROM numbers), 0) + 1)
        """))

        result = conn.execute(text("SELECT MAX(value) FROM numbers"))
        current_value = result.scalar()

    return f"Current number in DB: {current_value}"


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)