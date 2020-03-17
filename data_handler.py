import csv
import os

answers_header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
question_header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

ANSWER_DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
QUESTION_DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'

ANSWER_CSV_LENGTH = int(sum(1 for row in csv.reader('sample_data/data.csv')) / 4 - 2)
QUESTION_CSV_LENGTH = int(sum(1 for row in csv.reader('sample_data/data.csv')) / 4 - 2)

TEMPLATE_HEADER = ['TITLE', 'DATE', 'VIEWS', 'VOTES']


def read_elements_csv(path):
    temp_lst = []
    with open(path) as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        header = data[0]
        for row in data[1:]:
            dictionary = {key: value for key, value in zip(header, row)}
            temp_lst.append(dictionary)
        print(*data[1:], sep="\n")
        print(QUESTION_CSV_LENGTH)
        print(ANSWER_CSV_LENGTH)
        return temp_lst


# def append_csv_by_row(path, row):



def add_element_csv(path, row, csv_length, filepath):
    print(csv_length)
    temp_lst = insert_element_csv(row, csv_length, path)

    with open(filepath, 'w') as file:
        csv_writer = csv.writer(file)
        for line in temp_lst:
            csv_writer.writerow(line.values())


def insert_element_csv(path, row, index, csv_length):
    temp_lst = read_elements_csv(path)
    zip_row = zip(temp_lst[0].keys(), row)
    dict_row = dict((key, value) for key, value in zip_row)
    print(dict_row)
    if index == csv_length:
        temp_lst.append(dict_row)
    else:
        temp_lst[index] = dict_row
    return temp_lst


def get_id(path):
    temp_lst = read_elements_csv(path)
    length = len(temp_lst) - 1
    # print(temp_lst[length]['id'])
    return int(temp_lst[length]['id']) + 1


def get_element_by_id(path, user_id, header):
    for elt in read_elements_csv(path, header):
        if elt['id'] == str(user_id):
            return elt
