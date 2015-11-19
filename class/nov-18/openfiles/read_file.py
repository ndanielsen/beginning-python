"""
Opening a text file and a csv file.

"""

textfile = 'example.txt'

### Open a text file

# with open(textfile, 'r') as filename:
#     data = filename.read()

# print data



### Open a csv file

import csv

with open('csvexample.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print row 





if __name__ == '__main__':
    print 'hello world'