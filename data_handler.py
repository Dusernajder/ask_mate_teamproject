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


def dicts_to_listoflist(dict__dicts, header_to_first_row):
    container = []
    # converts list of dict to list of list, append the header to the first list
    if type(dict__dicts) == list:
        container.append(header_to_first_row)
        for dict in dict__dicts:
            temp_lst = []
            for key, value in dict.items():
                temp_lst.append(value)
            container.append(temp_lst)
    # converts a simple dict to a list with the values
    else:
        for key, value in dict__dicts.items():
            container.append(value)
    return container


def write_table_to_file(file_name, table, separator=','):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")
