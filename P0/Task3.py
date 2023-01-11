"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

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
in Bangalore.
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

# Big-O is O(n^3)


def categorize_calls():
  code_message = "The numbers called by people in Bangalore have codes:"
  bangalore_to_bangalore_message = "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."

  bangalore_calls = []
  bangalore_to_bangalore_counter = 0

  for call in calls:
    if re.search("(080)", call[0]):
      bangalore_calls.append(call[3])
    elif re.search("(080)", call[1]):
      bangalore_to_bangalore_counter += 1
  bangalore_calls = sorted(bangalore_calls)

  for call in bangalore_calls:
    code_message += ("\n" + call)

  print(code_message)
  percentage_of_calls_b_to_b = str(round(((float(bangalore_to_bangalore_counter) / float(len(bangalore_calls))) * 100.00), 2))
  print("{} {}".format(percentage_of_calls_b_to_b, bangalore_to_bangalore_message))


categorize_calls()








