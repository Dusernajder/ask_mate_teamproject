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


if __name__ == "__main__":
    app.run(
        debug=True
    )
