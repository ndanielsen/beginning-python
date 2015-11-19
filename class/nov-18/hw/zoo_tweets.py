"""
HW for Intro to Python

18 November 2015

National Zoo Tweet Analysis Homework


"""
import csv # What does this do?

zoo_csv = 'zoo_tweets.csv' 

### Task 1a
### Open and read the csv file using the csv.reader function
### Hint: https://docs.python.org/2/library/csv.html
### Hint2: What is the delimiter in this file?

### Task 1b
### Create a list called tweet_list
### Using a for-loop, append all tweet_text in each row to tweet_list 
### Hint: This be the second (elem 2) of the list


tweet_list = []

with open(zoo_csv, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    for row in spamreader:
        tweet_list.append(row[2])

print tweet_list



### Task 2
### Assign a variable called header for the first row.
### Assign a variable called rows to all rows after the first. ie row 0
### How many tweets or rows are in this csv file?
### When is the time span of the tweets (first versus last)?





### Task 3
### Make an empty list called retweets
### Can you make a separate list of all retweets? 
### Hint: use a for loop to identify if a tweet starts with '.@'




### Task 4
### Make another empty list called hash_tags
### Using split() on each tweet, can you identify all the hashtags in each tweet add
### add them to the list called hash_tags?
### Hint: you'll need a a for loop and an if statement word[0] == '#'




### Task 5
### Make another list with all tweets that mention #pandastory




### Bonus
### Is there are day of the week that gets the most tweets with the #pandastory hashtag from the Zoo?