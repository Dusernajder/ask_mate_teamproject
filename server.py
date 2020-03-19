from flask import Flask, render_template, redirect, request, url_for, flash
import data_handler
from data_handler import QUESTION_DATA_FILE_PATH, question_header, ANSWER_DATA_FILE_PATH, answers_header, \
    TEMPLATE_HEADER, UPLOAD_FOLDER
from werkzeug.utils import secure_filename

import util
import os

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    questions = util.convert_timestamp_to_date(data_handler.read_elements_csv(QUESTION_DATA_FILE_PATH))
    return render_template('home.html', questions=questions, headers=TEMPLATE_HEADER)


@app.route('/question/<question_id>')
def show_question(question_id):
    selected_question = data_handler.get_element_by_id(QUESTION_DATA_FILE_PATH, question_id)
    answers = data_handler.get_element_by_id(ANSWER_DATA_FILE_PATH, question_id)
    return render_template('question.html', question=selected_question, answers=answers)


@app.route("/add-question", methods=["GET", "POST"])
def add_question():
    if request.method == 'POST':
        question_id = data_handler.get_id(data_handler.QUESTION_DATA_FILE_PATH)
        date = util.get_unix_time()
        view = 0
        vote = 0
        title = request.form['title']
        message = request.form['message']

        # You can NOT upload a question without a picture yet :(
        image = request.files['image']
        if image.filename != '':
            image.save(os.path.join(UPLOAD_FOLDER, secure_filename(image.filename)))

        row = [question_id, date, view, vote, title, message, image.filename]
        data_handler.append_csv_by_row(data_handler.QUESTION_DATA_FILE_PATH, row)

    return render_template('add_question.html')


@app.route('/answers/<question_id>', methods=['GET', 'POST'])
def answers(question_id):
    list_to_csv = []
    temp_lst = []

    question_dict = data_handler.get_element_by_id(QUESTION_DATA_FILE_PATH, question_id)
    answers = util.convert_timestamp_to_date(data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH))

    if request.method == 'POST':

        message = request.form['answer_message']

        answer_container = [str(data_handler.get_id(ANSWER_DATA_FILE_PATH)), str(util.get_unix_time()), '0',
                            question_id, message, ]

        for item in answer_container:
            temp_lst.append(item)

        list_to_csv.append(temp_lst)
        data_handler.append_csv_by_row(ANSWER_DATA_FILE_PATH, temp_lst)
        return redirect('/')

    return render_template('answers.html', question=question_dict, answers=answers)


@app.route('/answers/<answer_id>/vote_up', methods=['GET', 'POST'])
def up_vote_answers(answer_id):
    if request.method == 'POST':
        answers = data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH)

        data_handler.change_vote(answers, answer_id, 'increment')
        data_handler.update_csv('answer.csv', [list(answer.values()) for answer in answers], answers_header)

        question_id = data_handler.get_question_id(answer_id, answers)

        return redirect(f'/answers/{question_id}')


@app.route('/answers/<answer_id>/vote_down', methods=['GET', 'POST'])
def down_vote_answers(answer_id):
    if request.method == 'POST':
        answers = data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH)

        data_handler.change_vote(answers, answer_id, 'decrement')
        data_handler.update_csv('answer.csv', [list(answer.values()) for answer in answers], answers_header)
        question_id = data_handler.get_question_id(answer_id, answers)

        return redirect(f'/answers/{question_id}')


@app.route('/delete_question/<question_id>')
def delete_question(question_id):
    remove_from_qs = util.remove_question(question_id)
    remove_answers = util.remove_answers(question_id)
    data_handler.update_csv('question.csv', [list(dictionary.values()) for dictionary in remove_from_qs],
                            question_header)
    data_handler.update_csv('answer.csv', [list(dictionary.values()) for dictionary in remove_answers], answers_header)

    return redirect(request.url)


if __name__ == "__main__":
    app.run(
        debug=True
    )
