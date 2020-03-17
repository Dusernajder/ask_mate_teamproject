from datetime import datetime
import time

def convert_timestamp_to_date(data):
    for i in range(len(data)):
        data[i]['submission_time'] = datetime.utcfromtimestamp(int(data[i]['submission_time'])).strftime('%Y-%m-%d')
    return data

def get_unix_time():
    return str(time.time())[:8]