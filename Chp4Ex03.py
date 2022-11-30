#Author: Omar Yunis
#Date: March 04, 2021
#Description: Assignment 3 - Chapter 4 Exercise 3

#Tell the user how the program should operate
print('The following will prompt you to enter your monthly budget and then your individual monthly expenses. Enter a negative value to signal you have finished entering your expenses.')

#Ask user to enter their monthly budget
userBudget = float(input('Enter your monthly budget ($):'))

#Ask user to enter first expense
firstAmt = float(input('Enter your first monthly expense ($):'))

#Initialize total
total = 0

#If user enters 0 or negative number, then either they had no expense or may have accidentally entered a negative number. If they entered a positive number, add to running total
if firstAmt > 0 :
    total = total + firstAmt
else:
    total = 0
    print("You didn't have any expenses?")

#If the total is greater than 0, run the while loop. Keep asking the user to enter their expenses while keeping a running total. Break out of the loop when the user enters a negative number
if total > 0:
    askUser = True
    while askUser:
        newAmt = float(input('Enter your next monthly expense ($):'))
        if newAmt < 0 :
            print('Your total monthly expense is: $', format(total,'0.2f'), sep='')
            break
        else:
            total = total + newAmt
            
#Calculate the difference between the user's budget and their monthly expenses. Tell the user how much they were over or under budget.
budMinusTot = userBudget - total
if budMinusTot > 0 :
    print('You were $',budMinusTot,' under budget.',sep='')
elif budMinusTot < 0:
    print('You were $',-budMinusTot,' over budget.',sep='')
else:
    print('You were perfectly on budget.')