#Author: Omar Yunis
#Date: Mar 4, 2021
#Description: Assignment 2 - Chapter 3 Exercise 16

#Get year from user
year = int(input('What year is it?'))

#Use logic outlined in the problem to determine if the entered year is a leap year
if (year % 100 == 0) and (year % 400 == 0):
    print('In', year, 'February has 29 days.')
elif (year % 100 != 0) and (year % 4 == 0):
    print('In', year, 'February has 29 days.')
else:
    print('In', year, 'February has 28 days.')
    

