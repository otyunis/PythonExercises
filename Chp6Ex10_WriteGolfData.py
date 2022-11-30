#Author: Omar Yunis
#Date: 04/28/2021
#Description: Assignment 5 - Chapter 6 - Exercise 10

fname = 'golf.txt' #file name
with open(fname, 'a') as file: #open file using context manager in append mode
    test = True #initialize decision variable
    while test == True: #while decision varaible is true ask user if they would like to add another record
        addInquiry = input('Would you like to add a player and score (y/n)? ')
        if addInquiry != 'y': #if user does not answer with 'y' then break loop
            test = False
        else:
            playerName = input('Enter player name:') #ask user to enter player name
            playerScore = input('Enter player score:') #ask user to enter player score
            record = "{'PlayerName':'"+playerName+"','PlayerScore':"+playerScore+"}\n" #store record as string using dicitonary format with name and score fields
            file.write(record) #append file with record
            