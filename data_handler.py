import csv
import os

answers_header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
question_header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

ANSWER_DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
QUESTION_DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'

ANSWER_CSV_LENGTH = int(sum(1 for row in csv.reader('sample_data/data.csv')) / 4 - 2)
QUESTION_CSV_LENGTH = int(sum(1 for row in csv.reader('sample_data/data.csv')) / 4 - 2)

TEMPLATE_HEADER = ['TITLE', 'DATE', 'VIEWS', 'VOTES']

UPLOAD_FOLDER = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'static/images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def read_elements_csv(path):
    temp_lst = []
    with open(path) as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        fieldnames = data[0]
        for row in data[1:]:
            dictionary = {key: value for key, value in zip(fieldnames, row)}
            temp_lst.append(dictionary)
        return temp_lst


def append_csv_by_row(path, row):
    data = read_elements_csv(path)
    fieldnames = answers_header if path == ANSWER_DATA_FILE_PATH else question_header

    with open(path, 'w') as file:
        data.append(dict(zip(fieldnames, row)))
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for line in data:
            csv_writer.writerow(line)


def get_id(path):
    temp_lst = read_elements_csv(path)
    length = len(temp_lst) - 1
    return int(temp_lst[length]['id']) + 1


def get_element_by_id(path, target_id):
    for row in read_elements_csv(path):
        if row['id'] == str(target_id):
            return row


def update_csv(path, data, header):
    with open(f'sample_data/{path}', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)


def change_vote(lst_of_dict, id, expression):
    for actual_dict in lst_of_dict:
        for key, value in actual_dict.items():
            if key == 'id' and value == id:
                actual_dict['vote_number'] = \
                    str(int(actual_dict['vote_number']) + 1) \
                    if expression == "increment" else \
                    str(int(actual_dict['vote_number']) - 1)


def get_question_id(id, lst_of_dict):
    for target_dict in lst_of_dict:
        for key, value in target_dict.items():
            if key == 'id' and value == id:
                return target_dict['question_id']
