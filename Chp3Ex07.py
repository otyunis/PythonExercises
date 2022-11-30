#Author: Omar Yunis
#Date: Mar 4, 2021
#Description: Assignment 2 - Chapter 3 Exercise 07

primaryColors = ['red','yellow','blue'] #list of possible primary colors

#Obtain the user's first color and check to see if it is a primary color.
#If it is a primary color move on by changing the flag to false.
#If it is not a valid color then repeat the loop until the user enters a valid color.
testOne = True 
while testOne:
    colorOne = input('What is the first primary color you want to mix?')
    if not colorOne in primaryColors:
        print('Error: You must enter either: "red", "yellow", or "blue"')
        testOne = True
    else:
        testOne = False
        
#Obtain the user's first color and check to see if it is a primary color.
#If it is a primary color move on by changing the flag to false.
#If it is not a valid color then repeat the loop until the user enters a valid color.
testTwo = True
while testTwo:
    colorTwo = input('What is the second primary color you want to mix?')
    if not colorTwo in primaryColors:
        print('You must enter either: "red", "yellow", or "blue"')
        testTwo = True
    else:
        testTwo = False

#For any combination of valid user inputs, display a message to the user tell 
#them what their colors mix to make (using logical comparisons). 
if colorOne == 'red' and colorTwo == 'red':
    print('When you mix',colorOne, 'and', colorTwo, 'you get red.')
elif colorOne == 'yellow' and colorTwo == 'yellow':
    print('When you mix',colorOne, 'and', colorTwo, 'you get yellow.')
elif colorOne == 'blue' and colorTwo == 'blue':
    print('When you mix',colorOne, 'and', colorTwo, 'you get blue.')
elif (colorOne == 'red' and colorTwo == 'blue') or (colorOne == 'blue' and colorTwo == 'red'):
    print('When you mix',colorOne, 'and', colorTwo, 'you get purple.')   
elif (colorOne == 'red' and colorTwo == 'yellow') or (colorOne == 'yellow' and colorTwo == 'red'):
    print('When you mix',colorOne, 'and', colorTwo, 'you get orange.')
elif (colorOne == 'blue' and colorTwo == 'yellow') or (colorOne == 'yellow' and colorTwo == 'blue'):
    print('When you mix',colorOne, 'and', colorTwo, 'you get green.')
else:
    print('You broke the program logic somehow.')