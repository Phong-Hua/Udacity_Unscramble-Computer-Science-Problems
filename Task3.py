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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def partA(callList: list):
    """Find all of the area codes and mobile prefixes called by people in Bangalore (080).
    - Fixed lines start with an area code enclosed in brackets. The area
        codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
        of the number to help readability. The prefix of a mobile number
        is its first four digits, and they always start with 7, 8 or 9.  
    INPUT:
      calls: a list of calls.
    OUTPUT:
      a list of unique area codes or mobile prefixes, sorted in alphabet.
    """
    incoming_area_mobile = set()
    for call in callList:
        if (call[0][:5] == '(080)'):
            # fix line number
            first_character = call[1][:1]
            if first_character == '(':
                close_parentheses_index = call[1].index(')')
                if (close_parentheses_index > 2):
                    area_code = call[1][:close_parentheses_index + 1]
                    incoming_area_mobile.add(area_code)
            # mobile number
            elif first_character == '7' or first_character == '8' or first_character == '9':
                mobile_number = call[1][:4]
                incoming_area_mobile.add(mobile_number)
    incoming_area_mobile_list = list(incoming_area_mobile)
    incoming_area_mobile_list.sort()
    return incoming_area_mobile_list

print("The numbers called by people in Bangalore have codes:")
for number in partA(calls):
  print(number)

def partB(callList: list):
  """Find percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore
  INPUT:
    callList: a list of calls.
  OUTPUT:
    percentage in decimal.
  """
  all_calls_count = 0;  # all calls made from Bangalore
  call_to_Bangalore_count = 0; # all calls made from Bangalore to Bangalore
  for call in callList:
    if (call[0][:5] == '(080)'):
      all_calls_count += 1;
      if (call[1][:5] == '(080)'):
        call_to_Bangalore_count += 1;
  return call_to_Bangalore_count * 100 / all_calls_count;

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format("{:.2f}".format(partB(calls))))

