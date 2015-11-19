
# EXERCISE: Write a program that prints the numbers from 1 to 100. But for
# multiples of 3 print 'fizz' instead of the number, and for the multiples of
# 5 print 'buzz'. For numbers which are multiples of both 3 and 5 print 'fizzbuzz'.

def fizz_buzz():
    nums = range(1, 101)    
    for num in nums:
        if num % 15 == 0:
            print 'fizzbuzz'
        elif num % 3 == 0:
            print 'fizz'
        elif num % 5 == 0:
            print 'buzz'
        else:
            print num

fizz_buzz()


# EXERCISE: Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] returns
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

def front_x(words):
    lista=[]
    listb=[]    
    for word in words:
        if word[0]=='x':
            lista.append(word)
        else:
            listb.append(word)
    return sorted(lista) + sorted(listb)

front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])