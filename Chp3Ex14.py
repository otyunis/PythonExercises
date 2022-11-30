#Author: Omar Yunis
#Date: Mar 4, 2021
#Description: Assignment 2 - Chapter 3 Exercise 14

#Get user's weight and height in lbs and inches
userWeight = float(input('Please enter your weight in lbs:'))
userHeight = float(input('Please enter your height in inches:'))

#Declare formula constant (based on lbs and inches)
BMI_CONST_INCHES_LBS = 703

#Calculate the user's BMI based on BMI formula
userBMI = userWeight*(BMI_CONST_INCHES_LBS)/(userHeight**2)

#Display the user's BMI
print('Your BMI is: ', format(userBMI,'.2f'))

#Determine which range the user's BMI falls into and tell the user if they are
#overweight, optimal weight, or underweight
if 18.5 <= userBMI <= 25:
    print('Your BMI is optimal.')
elif userBMI < 18.5:
    print('You are underweight.')
elif userBMI > 25:
    print('You are overweight.')
else:
    print('You broke the program logic somehow.')