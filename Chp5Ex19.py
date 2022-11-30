#Author: Omar Yunis
#Date: 04/16/2021
#Description: Assignment 4 - Chapter 5 - Exercise 19

#MAIN
def main():
    presVal = float(input('What is the present account value ($)?\n'))
    intRateMonthly = float(input('What is the monthly interest rate (%)?\n'))/100
    numMonths = float(input('How many months will the money be left in your account (#)?\n'))
    futureValue = future_value(presVal,intRateMonthly,numMonths)
    print('After {:.2f} months the value will be ${:.2f}.'.format(numMonths,futureValue))
    
#FUNCTIONS  
def future_value(presVal,intRateMonthly,numMonths):
    futureValue = presVal*(1+intRateMonthly)**numMonths
    return futureValue

if __name__ == '__main__':
    main()

