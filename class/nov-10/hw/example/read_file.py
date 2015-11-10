"""
Opening a text file and a csv file.

"""

textfile = 'example.txt'

with open(textfile, 'r') as f:
    read_data = f.read()

print type(read_data)

import csv

with open('csvexample.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print ', '.join(row)






if __name__ == '__main__':
    print 'hello world'