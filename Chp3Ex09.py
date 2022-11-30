#Author: Omar Yunis
#Date: Mar 4, 2021
#Description: Assignment 2 - Chapter 3 Exercise 09

#Prompt user to enter a pocket number until the user enters a number between 0 and 36
test = True 
while test:
    pocketNum = int(input('What is your pocket number?'))
    if not (0 <= pocketNum <= 36):
        print('Error: You must enter a number between 0 and 36')
        test = True
    else:
        test = False
        
#If the pocket number is between 1 and 10 or 19 and 28, then use modular division
#to determine if the number is even or odd and disply the appropriate pocket color
if (1 <= pocketNum <= 10) or (19 <= pocketNum <= 28):
    if pocketNum % 2 == 1:
        print('Your pocket is red.')
    else:
        print('Your pocket is black.')
        
#If the pocket number is between 11 and 18 or 29 and 36, then use modular division
#to determine if the number is even or odd and disply the appropriate pocket color
if (11 <= pocketNum <= 18) or (29 <= pocketNum <= 36):
    if pocketNum % 2 == 1:
        print('Your pocket is black.')
    else:
        print('Your pocket is red.')
        