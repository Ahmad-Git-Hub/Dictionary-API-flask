from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data_frame = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def result(word):

    definition = data_frame.loc[data_frame['word'] == word]['definition'].squeeze()
    dictionary_result = {'word': word, 'definition': definition}
    return dictionary_result


if __name__ == "__main__":
    app.run(debug=True, port=5001)