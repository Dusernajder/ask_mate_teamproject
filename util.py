from datetime import datetime
from time import time
import data_handler


def convert_timestamp_to_date(data):
    for i in range(len(data)):
        data[i]['submission_time'] = datetime.utcfromtimestamp(int(data[i]['submission_time'])).strftime('%Y-%m-%d')
    return data


def get_unix_time():
    return str(int(time()))


def sort(path, order):
    data = data_handler.read_elements_csv(path)
    return sorted(data, key=lambda item: item[order])
