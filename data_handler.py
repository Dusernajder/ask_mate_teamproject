import csv
import os

answers_header = ['id','submission_time','vote_number','question_id','message','image']
question_header = ['id','submission_time','view_number','vote_number','title,message','image']

ANSWER_DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
QUESTION_DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'


def read_elements_csv(path):
    temp_lst = []
    with open(path) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dictionary = {key: value for key, value in zip(answers_header, row)}
            temp_lst.append(dictionary)
        return temp_lst
