from flask import Flask
from app import run_parsing
import pandas as pd


app = Flask(__name__)

@app.route('/')
def hello_world():
    run_parsing("out.csv")
    return csvToList("out.csv")

def csvToList(data):
    df = pd.read_csv(data)
    answers = [['product_name |', ' mount |', ' article |', ' width |', ' height |', ' depth |']]

    for line_iter in range(len(df)):
        line = []
        for column_iter in range(len(df.columns)):
            line.append(df.iloc[line_iter, column_iter])
            line.append(' | ')
        answers.append(str("\n" + 60 * "-" + "\n"))
        answers.append(line)

    return answers

if __name__ == '__main__':
    app.run(debug=True)