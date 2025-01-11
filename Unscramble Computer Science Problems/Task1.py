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
 There are 570 different telephone numbers in the records.
"""
"""
# TASK 1:
# Create a set to store unique telephone numbers
"""
unique_numbers = set()

"""
# Add all numbers from texts dataset
"""
for record in texts:
    unique_numbers.add(record[0]) # Adding sending number
    unique_numbers.add(record[1]) # Adding receiving number

"""
# Add all numbers from calls dataset
"""
for record in calls:
    unique_numbers.add(record[0]) # Adding calling number
    unique_numbers.add(record[1]) # Adding receiving number
    
"""
# Count of unique telephone numbers
"""
count_unique_numbers = len(unique_numbers)

"""
# Print the result
"""
print(f"There are {count_unique_numbers} different telephone numbers in the records.")
