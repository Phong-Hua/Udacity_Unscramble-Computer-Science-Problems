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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def task4(textList: list, callList: list):
    """
    Create a set of possible telemarketers: these are numbers that make outgoing calls but never send texts,
    receive texts or receive incoming calls.
    INPUT:
    callList: a list of calls.
    textList: a list of texts.
    OUTPUT:
    a list of number that possible for telemarketers.
    """
    send_text_set = set()
    receive_text_set = set()
    make_call_set = set()
    receive_call_set = set()
    telemarketers_set = set()

    for text in textList:
        send_text_set.add(text[0])
        receive_text_set.add(text[1])
    for call in callList:
        make_call_set.add(call[0])
        receive_call_set.add(call[1])
    for number in make_call_set:
        if (number not in send_text_set) and (number not in receive_text_set) and (number not in receive_call_set):
            telemarketers_set.add(number);
            
    telemarketers_list = list(telemarketers_set)
    telemarketers_list.sort()
    return telemarketers_list;

def print_task4(textList: list, callList: list):
    print(f"These numbers could be telemarketers:")
    telemarketers_number = task4(textList, callList);
    for number in telemarketers_number:
        print(number)

print_task4(texts, calls);
