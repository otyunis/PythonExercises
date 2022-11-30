#Author: Omar Yunis
#Date: March 04, 2021
#Description: Assignment 3 - Chapter 4 Exercise 8

print('The following will prompt you to answer a sequence of positive numbers. Enter a negative number to indicate the end of the sequence.')

firstNum = float(input('Enter your first positive number:'))

#Initialize total
total = 0

#If user enters a negative number, then tell the user that they didn't enter any positive numbers. If they enter a 0 then tell the user the sum is 0.
if firstNum > 0 :
    total = total + firstNum
elif firstNum == 0:
    print('The sum of the numbers you entered is 0.')
else:
    total = 0
    print("You didn't enter any positive numbers.")

#If the total is greater than 0, run the while loop. Keep asking the user to enter positive numbers while keeping a running sum. Break out of the loop when the user enters a negative number.
if total > 0:
    askUser = True
    while askUser:
        newAmt = float(input('Enter your next positve number:'))
        if newAmt < 0 :
            print('The sum of the numbers you entered is: ', format(total,'0.2f'), sep='')
            break
        else:
            total = total + newAmt
