from flask import Flask, render_template, redirect, request, url_for
import data_handler
from data_handler import QUESTION_DATA_FILE_PATH, question_header
import util

app = Flask(__name__)


@app.route("/")
def home():
    questions = data_handler.read_elements_csv(QUESTION_DATA_FILE_PATH, question_header)
    questions = util.convert_timestamp(questions)
    return render_template('home.html', questions=questions)


@app.route("/add-question", methods=["GET, POST"])
def add_question():

    if request.method == 'POST':
        return redirect("/")

    return render_template('')

    return render_template('add_question.html')


if __name__ == "__main__":
    app.run(
        debug=True
    )
