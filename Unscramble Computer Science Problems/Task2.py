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
(080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
"""
"""
# TASK 2: Longest time spent on phone
"""
phone_time = {}

"""
# Loop through each record in the calls dataset
"""
for record in calls:
    calling_number = record[0]
    receiving_number = record[1]
    duration = int(record[3])  # Convert duration to integer
    
    """
    # Add duration to the calling number's total
    """
    if calling_number not in phone_time:
        phone_time[calling_number] = duration
    else:
        phone_time[calling_number] += duration
    """
    # Add duration to the receiving number's total
    """
    if receiving_number not in phone_time:
        phone_time[receiving_number] = duration
    else:
        phone_time[receiving_number] += duration
"""
# Find the telephone number with the longest total time
"""
longest_time_number = max(phone_time, key=phone_time.get)
longest_time = phone_time[longest_time_number]

"""
# Print the result
"""
print(f"{longest_time_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.")
