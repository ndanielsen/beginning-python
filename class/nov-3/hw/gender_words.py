#!/usr/bin/python -tt

"""
Gender words for HW

Count the number of gender words in your favorite book on project gutenberg. 

"""

MALE_WORDS=set(['guy','spokesman','chairman',"men's",'men','him',"he's",'his',
    'boy','boyfriend','boyfriends','boys','brother','brothers','dad',
    'dads','dude','father','fathers','fiance','gentleman','gentlemen',
    'god','grandfather','grandpa','grandson','groom','he','himself',
    'husband','husbands','king','male','man','mr','nephew','nephews',
    'priest','prince','son','sons','uncle','uncles','waiter','widower',
    'widowers'])
FEMALE_WORDS=set(['heroine','spokeswoman','chairwoman',"women's",'actress','women',
    "she's",'her','aunt','aunts','bride','daughter','daughters','female',
    'fiancee','girl','girlfriend','girlfriends','girls','goddess',
    'granddaughter','grandma','grandmother','herself','ladies','lady',
    'lady','mom','moms','mother','mothers','mrs','ms','niece','nieces',
    'priestess','princess','queens','she','sister','sisters','waitress',
    'widow','widows','wife','wives','woman'])

### Step one
#1 Download your book as a text file into the hw directory.

#2 Open the txt file with the 'with' statement as in read_file.py

#3 Define several variables named male_words_count, female_words_count 
#  and neutral_words_count. Assign their starting value as zero. 

#4 Figure out how to tokenize the text file or split() all the text into
# individual words in a list. For example, turn 'I like puppies' into 
# ['I', 'like', 'puppies']

#5 Using a for loop on the txt file (now a list of strings), see if a word is in
# MALE_WORDS or in FEMALE_WORDS. If a word is in one, add +1 to female_words_count 
# or male_words_count. Else, add one to neutral_words_count.

# hint: https://docs.python.org/2/tutorial/datastructures.html#sets

# Do some basic math. What are the total words? 
# Print out your findings and comment on them. 

### Bonus: 
### 1. Write a function and try this on another book. What do you notice?
### 2a. Make a new list of words that you want to count. 
### 2b. Can you figure out a way to count all the words in your new list?
### Hint: Try to do this a dictionary. 
### https://docs.python.org/2/tutorial/datastructures.html#dictionaries  









if __name__ == '__main__':
    print MALE_WORDS, FEMALE_WORDS