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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def task1(textList: list, callList: list):
    """
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    all_telephones = set()

    for text in textList:
        all_telephones.add(text[0])
        all_telephones.add(text[1])

    for call in callList:
        all_telephones.add(call[0])
        all_telephones.add(call[1])

    print("There are {} different telephone numbers in the records.".format(len(all_telephones)))

task1(texts, calls);