from datetime import datetime
from time import time
import data_handler


def convert_timestamp_to_date_dict(data):
    for i in range(len(data)):
        data[i]['submission_time'] = datetime.utcfromtimestamp(int(data[i]['submission_time'])).strftime('%Y-%m-%d')
    return data


def get_unix_time():
    return str(int(time()))


def sort(path, order):
    data = data_handler.read_elements_csv(path)
    return sorted(data, key=lambda item: item[order])


def remove_question(question_id):
    questions = data_handler.read_elements_csv(data_handler.QUESTION_DATA_FILE_PATH)
    for i, question in enumerate(questions):
        if question['id'] == question_id:
            del questions[i]
    return questions


def remove_answers(question_id):
    answers = data_handler.read_elements_csv(data_handler.ANSWER_DATA_FILE_PATH)
    for i, answer in enumerate(answers):
        if answer['id'] == question_id:
            del answers[i]
    return answers


def convert_timestamp_to_date_string(ts):
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d')
