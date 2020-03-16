from datetime import datetime

def convert_timestamp(data):
    for i in range(len(data)):
        data[i]['submission_time'] = datetime.utcfromtimestamp(int(data[i]['submission_time'])).strftime('%Y-%m-%d')
    return data
