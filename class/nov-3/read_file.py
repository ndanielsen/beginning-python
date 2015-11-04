"""
Opening a text file and a csv file.

Nathan 
"""

# textfile = 'example.txt'

# with open(textfile, 'r') as f:
#     read_data = f.read()

# print type(read_data)

import csv

with open('csvexample.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print ', '.join(row)







# print 'hello all'