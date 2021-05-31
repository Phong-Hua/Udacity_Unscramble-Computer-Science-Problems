"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def task0(textList, callList):
    """
    Print messages:
    "First record of texts, <incoming number> texts <answering number> at time <time>"
    "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
    """
    text_incoming_number, text_answering_number, text_time = textList[0]
    print(f"First record of texts, {text_incoming_number} texts {text_answering_number} at time {text_time}")

    call_incoming_number, call_answering_number, call_time, call_duration = callList[len(calls)-1]
    print(f"Last record of calls, {call_incoming_number} calls {call_answering_number} at time {call_time}, lasting {call_duration} seconds")

task0(texts, calls);