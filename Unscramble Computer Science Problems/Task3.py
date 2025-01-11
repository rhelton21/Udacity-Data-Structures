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


"""
TASK 3:
Part A: Find all of the area codes and mobile prefixes called by people in Bangalore.
Part B: Calculate the percentage of calls from Bangalore to Bangalore.
"""

"""
# Helper function to check if the number is a Bangalore number
"""
def is_bangalore_number(number):
    return number.startswith("(080)")

"""
# Helper function to extract the area code or mobile prefix from the number
"""
def extract_code(number):
    if number.startswith("("):
        return number.split(')')[0] + ")"
    elif " " in number:
        return number[:4]
    return number[:3]  # For telemarketers

"""
# Part A: Area codes and mobile prefixes called by Bangalore numbers
"""
codes_called_by_bangalore = set()

"""
# Part B: Counts for calculating percentages
"""
bangalore_to_bangalore_calls = 0
total_bangalore_calls = 0

for call in calls:
    calling_number = call[0]
    receiving_number = call[1]

    if is_bangalore_number(calling_number):
        total_bangalore_calls += 1
        codes_called_by_bangalore.add(extract_code(receiving_number))

        if is_bangalore_number(receiving_number):
            bangalore_to_bangalore_calls += 1

"""
# Part A: Print the codes
"""
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes_called_by_bangalore):
    print(code)

"""
# Part B: Calculate and print the percentage
"""
percentage = bangalore_to_bangalore_calls / total_bangalore_calls * 100
print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
The numbers called by people in Bangalore have codes:
(022)
(040)
(04344)
(044)
(04546)
(0471)
(080)
(0821)
7406
7795
7813
7829
8151
8152
8301
8431
8714
9008
9019
9035
9036
9241
9242
9341
9342
9343
9400
9448
9449
9526
9656
9738
9740
9741
9742
9844
9845
9900
9961
24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
"""

