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


"""
TASK 4:
Identify possible telemarketers.
"""

"""
# Collect all numbers that send or receive texts, and receive calls
"""
non_telemarketers = set()
for text in texts:
    non_telemarketers.add(text[0])  # Sending texts
    non_telemarketers.add(text[1])  # Receiving texts

for call in calls:
    non_telemarketers.add(call[1])  # Receiving calls

"""
# Collect all numbers that make outgoing calls
"""
outgoing_calls = set(call[0] for call in calls)

"""
# Potential telemarketers are those who make outgoing calls but are not in non_telemarketers
"""
potential_telemarketers = outgoing_calls - non_telemarketers

"""
# Print the potential telemarketers
"""
print("These numbers could be telemarketers: ")
for number in sorted(potential_telemarketers):
    print(number)


"""
These numbers could be telemarketers:
(022)37572285
(022)65548497
(022)68535788
(022)69042431
(040)30429041
(044)22020822
(0471)2171438
(0471)6579079
(080)20383942
(080)25820765
(080)31606520
(080)40362016
(080)60463379
(080)60998034
(080)62963633
(080)64015211
(080)69887826
(0821)3257740
1400481538
1401747654
1402316533
1403072432
1403579926
1404073047
1404368883
1404787681
1407539117
1408371942
1408409918
1408672243
1409421631
1409668775
1409994233
74064 66270
78291 94593
87144 55014
90351 90193
92414 69419
94495 03761
97404 30456
97407 84573
97442 45192
99617 25274
"""