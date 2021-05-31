"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def task2(callList: list):
    """
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during 
    September 2016.".
    """
    time_dict = {}
    for call in callList:
        time_dict[call[0]] = time_dict.get(call[0], 0) + int(call[3])
        time_dict[call[1]] = time_dict.get(call[1], 0) + int(call[3])

    telephone_number = max(time_dict, key = lambda k: time_dict.get(k));
    max_duration = time_dict.get(telephone_number);

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone_number, max_duration))

task2(calls);