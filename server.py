from flask import Flask, render_template, redirect, request, url_for
import data_handler
from data_handler import QUESTION_DATA_FILE_PATH, question_header, ANSWER_DATA_FILE_PATH, answers_header, \
    TEMPLATE_HEADER
import util
import os

app = Flask(__name__)


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
        # image = 'image.jpg'
        image = request.form['image']
        # print(img)

        row = [question_id, date, view, vote, title, message, image]
        data_handler.append_csv_by_row(data_handler.QUESTION_DATA_FILE_PATH, row)

        return redirect("/")

    return render_template('add_question.html')


app.config['UPLOAD_IMAGE'] = '/home/dani/PycharmProjects/ask_mate_teamproject/static/image'


@app.route('/answers/<question_id>', methods=['GET', 'POST'])
def answers(question_id):
    list_to_csv = []
    temp_lst = []

    question_dict = data_handler.get_element_by_id(QUESTION_DATA_FILE_PATH, question_id)
    answers = data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH)

    if request.method == 'POST':

        message = request.form['answer_message']

        answer_container = [str(data_handler.get_id(ANSWER_DATA_FILE_PATH)), str(util.get_unix_time()), '0',
                            question_id, message, ]

        for item in answer_container:
            temp_lst.append(item)

        print(temp_lst)
        list_to_csv.append(temp_lst)
        data_handler.append_csv_by_row(ANSWER_DATA_FILE_PATH, temp_lst)
        return redirect('/')

    return render_template('answers.html', question=question_dict, answers=answers, )


@app.route('/answers/<answer_id>/vote_up', methods=['GET', 'POST'])
def up_vote_answers(answer_id):
    if request.method == 'POST':
        answers = data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH)

        for dict in answers:
            for key, value in dict.items():
                if key == 'id' and value == answer_id:
                    print(dict['vote_number'])
                    dict['vote_number'] = str(int(dict['vote_number']) + 1)
            print(dict)
        lists_to_write = data_handler.dicts_to_listoflist(answers, answers_header)
        data_handler.write_table_to_file(ANSWER_DATA_FILE_PATH, lists_to_write, ',')

    return redirect('/')


@app.route('/answers/<answer_id>/vote_down', methods=['GET', 'POST'])
def down_vote_answers(answer_id):
    if request.method == 'POST':
        answers = data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH)

        for dict in answers:
            for key, value in dict.items():
                if key == 'id' and value == answer_id:
                    print(dict['vote_number'])
                    dict['vote_number'] = str(int(dict['vote_number']) - 1)
            print(dict)
        lists_to_write = data_handler.dicts_to_listoflist(answers, answers_header)
        data_handler.write_table_to_file(ANSWER_DATA_FILE_PATH, lists_to_write, ',')

    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True
    )
