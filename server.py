from flask import Flask, render_template, redirect, request, url_for
import data_handler
from data_handler import QUESTION_DATA_FILE_PATH, question_header, ANSWER_DATA_FILE_PATH, answers_header, TEMPLATE_HEADER
import util

app = Flask(__name__)


@app.route("/")
def home():
    questions = data_handler.read_elements_csv(QUESTION_DATA_FILE_PATH, question_header)
    questions = util.convert_timestamp(questions)
    return render_template('home.html', questions=questions, headers=TEMPLATE_HEADER)


@app.route('/question/<question_id>')
def show_question(question_id):
    selected_question = data_handler.get_element_by_id(QUESTION_DATA_FILE_PATH, question_id, question_header)
    answers = data_handler.get_element_by_id(ANSWER_DATA_FILE_PATH, question_id, answers_header)
    return render_template('question.html', question=selected_question, answers=answers)


@app.route("/add-question", methods=["GET, POST"])
def add_question():

    if request.method == 'POST':
        question_id = data_handler.get_id(data_handler.QUESTION_DATA_FILE_PATH)
        title = request.form['title']
        message = request.form['message']

        return redirect("/")

    return render_template('add_question-html')


if __name__ == "__main__":
    app.run(
        debug=True
    )
