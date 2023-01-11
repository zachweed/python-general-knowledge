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

# Big-O of O(n^4)

def number_sent_text(number):
  for text in texts:
    sender = text[0]
    if sender == number:
      return True
  return False

def number_received_text(number):
  for text in texts:
    receiver = text[1]
    if receiver == number:
      return True
  return False

def number_received_call(number):
  for call in calls:
    receiver = call[1]
    if receiver == number:
      return True
  return False


telemarketers_string = ""
telemarketers = []

for call in calls:
  telephone_number = call[0]
  if (not number_sent_text(telephone_number) or not number_received_text(telephone_number) or not number_received_call(telephone_number)):
    if (telephone_number not in telemarketers):
      telemarketers.append(telephone_number)

telemarketers = sorted(telemarketers)
for telemarketer in telemarketers:
  telemarketers_string += ("\n" + telemarketer)

message = 'These numbers could be telemarketers:\n\n {}'.format(telemarketers_string)

print(message)



