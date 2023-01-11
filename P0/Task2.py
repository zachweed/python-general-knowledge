import datetime

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

# Big O is O(n)

call_details = []

for call in calls:
  call_number = call[1]
  call_date = call[2]
  call_duration = int(call[3])
  if any(call_details):
    if call_duration > call_details[2]:
      call_details = [call_number, call_date, call_duration]
  else:
    call_details = [call_number, call_date, call_duration]

print(f'{call_details[0]} spend the longest time, {call_details[2]} seconds, on the phone during {datetime.datetime.strptime(call_details[1], "%m-%d-%Y %H:%M:%S")}.')
