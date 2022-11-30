#Author: Omar Yunis
#Date: March 4, 2021
#Description: Assignment 3 - Chapter 4 Exercise 13

#Get starting population, growth rate, and number of days from user. Convert rate percentage to decimal.
startPop = int(input('What is the starting population?'))
growthRate = float(input('What is the growth rate (%)?').replace('%',''))/100
daysGrowing = int(input('How many days will the population be left to grow?'))

#For each day, calculate the population for that day based on repeatedly multiplying by the population by the growth rate (i.e. exponentiation of the starting population). Shift d by one to fit problem convention. Display population for each day to user. 
for d in range(daysGrowing):
    currentPop = startPop*((1+growthRate)**d)
    print('The population on day',d+1,'is:',format(currentPop,'.2f'))

