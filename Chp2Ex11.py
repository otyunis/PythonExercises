# Author: Omar Yunis
# Date: Feb 18, 2021
# Assignment: Chapter 2 Exercise 11

# Problem statement: Write a program that asks the user for the number of 
# males and the number of females registered in the class. The program should
# display the percentage of males and females in the class. 

# Request user for number of males and females in the class
males = int(input('How many males are in the class?\n'))
females = int(input('How many females are in the class?\n'))

# Calculate the percent of males and females in the class
totalPop = males+females
percentMale = males/totalPop*100
percentFemale = females/totalPop*100

# Display the percentage of males and females in the class to the user
print('Percentage of males in class: ',format(percentMale, '.2f'),'%','\n'\
      'Percentage of females in class: ',format(percentFemale, '.2f'),'%',sep=(''))
