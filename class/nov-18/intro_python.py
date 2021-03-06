"""
GA - Introduction to Python

DATE - 18 November 2015

Instructor - Nathan Danielsen

https://github.com/ndanielsen/beginning-python/

tree/master/class/nov-18
"""

print 'hello'

# BASIC DATA TYPES

# Numbers
# https://docs.python.org/2/tutorial/introduction.html#numbers

5       # Integer 
5.0     # Float (decimal)
x = 5               # creates an object

print type(x)       # check the type: int (not declared explicitly)
type(x)             # automatically prints
type(5)             # assigning it to a variable is not required

type(5.0)           # float
type(True)          # bool


# math operations

1 + 2       # Addition
7 - 5       # Division
5 * 7       # Multiplication 
10 / 3      # Division
10 / 3.0    # Floor division
16 % 5      # Modulo (remainder)
2**10        # Exponent

# variable assignment

a = 1
b = 2
c = 6

d = a + b - c
print d

e = d / 6.0
print e


# STRINGS
# https://docs.python.org/2/tutorial/introduction.html#strings

type('string')        # str

s = str(42)   
s      # convert another data type into a string (casting)
s = 'I like you'

# examine a string
s[0]                # returns 'I'
len(s)              # returns 10

# string slicing like lists
s[0:7]               # returns 'I like'
s[6:]               # returns 'you'
s[-1]               # returns 'u'

# EXERCISE: Book Titles (Part 1)
# 1) Extract the book title from the string
# 2) Save each book title to a variable (ie book1_title)
# 3) How many characters/elements are in each title?

book1 = "Beyond the Door by Dick, Philip K., 1928-1982"
book1_title = book1[:15]
book1[-26:]

len(book1_title)

book1_title

book2 = "The Variable Man by Dick, Philip K., 1928-1982"
book2_title = book2[:12]
book2_title

book2[:-30]

book3 = "The Skull by Dick, Philip K., 1928-1982"

book3_title = book3[:-30]




################

# split a string into a list of substrings separated by a delimiter

s = 'I like you'
s.split(' ')        # returns ['I','like','you']
s.split()           # same thing

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# EXERCISE: Book Titles (Part 2)
# 1. How words are book1_title? 
# BONUS: Comparison:  Does book1_title have more words then book3_title3?
# HINT: https://docs.python.org/2/library/stdtypes.html#comparisons
book1 = "Beyond the Door by Dick, Philip K., 1928-1982"
book1_title = book1[:15]

book1_words = book1_title.split()

len(book1_words)

len(book3_title.split())

# LISTS
# https://docs.python.org/2/tutorial/introduction.html#lists

nums = [5, 5.0, 'five']     # multiple data types
nums                        # print the list
type(nums)                  # check the type: list
len(nums)                   # check the length: 3
nums[0]                     # print first element
nums[0] = 6                 # replace a list element

nums

nums.append(7)              # list 'method' that modifies the list
help(nums.append)           # help on this method
help(nums)     

dir(nums)
             # help on a list object
nums.remove('five')         # another list method

nums

sorted(nums)                # 'function' that does not modify the list
nums                        # it was not affected
nums = sorted(nums) 
nums        # overwrite the original list
sorted(nums, reverse=True)  # optional argument

# list slicing [start:end:stride]
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
test = weekdays[3:]        # elements 3, 4

weekdays

weekdays[-2]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

# EXERCISE - 
# Add/ concatentate 'sat' and 'sun' to the weekdays list.
# Assign this to new a variable called days

weekdays.append('sat')
weekdays.append('sun')

weekend = ['sat', 'sun']

days = weekdays + weekend

weekdays + ['sat'] + ['sun']

days

# FOR LOOPS
# https://docs.python.org/2/tutorial/controlflow.html#for-statements

# range returns a list of integers
range(5)     # returns [0, 1, 2]: includes first value but excludes second value
range(30)        # same thing: starting at zero is the default


# simple for loop
for num in range(5):
    print 'hello: ' + str(num)

# print each list element in uppercase

fruits = ['apple', 'banana', 'cherry']

len(fruits)


for i in range(len(fruits)):
    upper_case = fruits[i].upper()    
    print upper_case
    

# better for loop
for space_fruit in fruits:
  print space_fruit.upper()





# BOOLEANS and COMPARISONS
# https://docs.python.org/2/library/stdtypes.html#comparisons

1 < 5  #strictly less than     
10 > 3  #strictly greater than        

100 == 100 #equal    
100 != 100 #not equal





# FLOW CONTROL
# https://docs.python.org/2/tutorial/controlflow.html

sam = 'sam'

if num %3 == 'ham':
    print 'do something'
elif sam == 'jam':
    print 'do something'
else:
    print 'green eggs and ham'

# EXERCISE
# Using a for loop, flow control and boolean logic, identify if 
# the documents are .docx, .csv or .ppt.
# Bonus: For each type create a list and append to it. 

documents = ['report1.docx', 'newproduct.ppt', 'report1data.csv', 
            'rawdata.csv', 'notes.docx', 'competitors.ppt',]

documents[0][-4:]
documents[1][-3:]
documents[2][-3:]

documents[0].split('.')[1]

for document in documents:
    document_split =  document.split('.')   
    document_suffix = document_split[1]
    
    if document_suffix == 'docx':
        print 'docx: ' + document
        
    elif document_suffix == 'ppt':
        print 'ppt: ' + document
    
    else:
        print 'csv: ' + document

import glob

glob.glob('*')




# FUNCTIONS

def give_me_five():         # function definition ends with colon
    return 5                # indentation required for function body

give_me_five()              # prints the return value (5)
num = give_me_five()        # assigns return value to a variable, doesn't print it

num


def add_two_numbers(x, y):
    return x + y

add_two_numbers(8, 9)



ops = 'add'

def calc(x, y, ops):         # three parameters (without any defaults)
    if ops == 'add':         # conditional statement
        return x + y
    elif ops == 'subtract':
        return x - y
    else:
        print 'Valid operations: add, subtract'

calc(5, 3, 'add')
calc(5, 3, 'subtract')
calc(5, 3, 'multiply')
calc(5, 3)


ops = 'add'

def calc_plus(x, y, ops='add'):         # three parameters (without any defaults)
    if ops == 'add':         # conditional statement
        return x + y
    elif ops == 'subtract':
        return x - y
    else:
        print 'Valid operations: add, subtract'

calc_plus(5, 3, ops='subtract')






# EXERCISE: Write a program that prints the numbers from 1 to 100. But for
# multiples of 3 print 'fizz' instead of the number, and for the multiples of
# 5 print 'buzz'. For numbers which are multiples of both 3 and 5 print 'fizzbuzz'.









# EXERCISE: Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] returns
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.






### HOMEWORK

# Homework Reading
# Learn about a data type that we didn't cover here tonight: dictionary
# http://www.diveintopython.net/native_data_types/

# Homework Assignment - National Zoo Tweet Analysis

# If you email or send me a gist of your code, I will do a code review and send you back
# the answers. 





