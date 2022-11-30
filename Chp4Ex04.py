#Author: Omar Yunis
#Date: March 04, 2021
#Description: Assignment 3 - Chapter 4 Exercise 4

#Ask the user for information on vehicle speed and travel duration
speed = float(input('What is the speed of the vehicle (mph)?'))
hours = int(input('How many hours has the vehicle travels (whole number)?'))

#From 0 up until the number of hours the user entered, calculate the distance traveled and display the distance traveled for each hour to the user
for hours in range(hours+1):
    distance  = speed*hours
    print('The car traveled',format(distance,'0.2f'),'miles in',hours,'hours.')