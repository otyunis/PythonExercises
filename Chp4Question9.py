#Author: Omar Yunis
#Date: March 4, 2021
#Description: Assignment 3 - Chapter 4 Question 9

numBase10 = int(input('Enter a positive integer in base 10:'))

quotient = numBase10 #initialize quotient as entered base 10 number

numBase2 = '' #initialize empty string for storing remainders
i = 0 #initialize counter
while quotient != 0:
    i += 1 #increment counter
    quotient = numBase10 // (2**i) #quotient after dividing by 2 i-times
    remainder = (numBase10 % (2**i)) // (2**(i-1)) #remainder after dividing by 2 i-times
    remainderStr = str(remainder) #convert remainder to string
    numBase2 = remainderStr + numBase2 #add remainder to base 2 number string
    
print(numBase10,'in base 10 =',numBase2,'in base 2.') #print number in base 2