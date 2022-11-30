# Author: Omar Yunis
# Date: Feb 18, 2021
# Assignment: Chapter 2 Exercise 14

# Problem statement: based on the equation A = P*(1+r/n)**(n*t), write a 
# program that calculates A (amount of money in account after specified number
# of years), based on P (principal amount), r (annual interest rate), n (number
# of times interest is compounded each year), and t (specified number of years)

# Request relevant values from user
principal_P = float(input('What is your principle amount ($)?\n'))
interestRate_r = float(input('What is the interest rate (%)?\n'))
compoundRate_n = float(input('How many times is interest compounded each year?\n'))
numYears_t = float(input('How many years will the account earn interest (years)?\n'))

# Calculate future amount based on user's inputs
futureAmount_A =principal_P*(1+interestRate_r/(100*compoundRate_n))**(compoundRate_n*numYears_t)

# Display future amount to user
print('There will be $', format(futureAmount_A,'.2f'),' in your account after ',\
      format(numYears_t,'.2f'),' years.',sep=(''))