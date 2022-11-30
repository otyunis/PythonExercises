#Author: Omar Yunis
#Date: March 4, 2021
#Description: Assignment 3 - Chapter 4 Problem 10

numBase10 = int(input('Enter a positive integer in base 10:'))

quotient = numBase10 #initialize quotient as entered base 10 number

numBase16 = '' #initialize empty string for storing remainders
i = 0 #initialize counter
while quotient != 0:
    i += 1 #increment counter
    quotient = numBase10 // (16**i) #quotient after dividing by 16 i-times
    remainder = (numBase10 % (16**i)) // (16**(i-1)) #remainder after dividing by 16 i-times
    ##Folowing if-elif-else used for converting remainders 10-15 to A-F
    if remainder == 10:
        remainderStr = 'A'
    elif remainder == 11:
        remainderStr = 'B'
    elif remainder == 12:
        remainderStr = 'C'
    elif remainder == 13:
        remainderStr = 'D'
    elif remainder == 14:
        remainderStr = 'E'
    elif remainder == 15:
        remainderStr = 'F'
    else:
        remainderStr = str(remainder) #convert remainder to string
    numBase16 = remainderStr + numBase16 #add remainder to base 16 number string
    
print(numBase10,'in base 10 =',numBase16,'in base 16.') #print number in base 16