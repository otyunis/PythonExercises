#Author: Omar Yunis
#Date: 04/28/2021
#Description: Assignment 5 - Chapter 6 - Exercise 10

fname = 'golf.txt' #file name
with open(fname, 'r') as file: #open record file in read mode using context manager
    print("{: ^20} | {: ^5}".format('PLAYER','SCORE'))
    for field in file: #iterate through each line in file
        nameScore = eval(field) #evaluate string as if it were python code (i.e. read in as a dictionary)
        print("{: ^20} | {: ^5}".format(nameScore['PlayerName'], nameScore['PlayerScore'])) #print the fields for each line in file
