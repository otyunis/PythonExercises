#Author: Omar Yunis
#Date: March 4, 2021
#Description: Assignment 3 - Chapter 4 Question 11

numBase10 = int(input('Enter a positive integer in base 10:'))
print('{:^5}'.format('Base 10'),'{:^10}'.format('Base 2'),'{:^5}'.format('Base 16')) #print number in base 16

#For intgers between 1 and the entered integer, convert to base 2 and 16 and display each iteration to user
for num in range(1,numBase10+1):
    quotient = num #initialize quotient as entered base 10 number
    numBase2 = '' #initialize empty string for storing remainders
    i = 0 #initialize counter
    while quotient != 0:
        i += 1 #increment counter
        quotient = num // (2**i) #quotient after dividing by 2 i-times
        remainder = (num % (2**i)) // (2**(i-1)) #remainder after dividing by 2 i-times
        remainderStr = str(remainder) #convert remainder to string
        numBase2 = remainderStr + numBase2 #add remainder to base 2 number string
    
    quotient = num
    numBase16 = '' #initialize empty string for storing remainders
    i = 0 #initialize counter
    while quotient != 0:
        i += 1 #increment counter
        quotient = num // (16**i) #quotient after dividing by 16 i-times
        remainder = (num % (16**i)) // (16**(i-1)) #remainder after dividing by 16 i-times
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
    
    print('{:>5}'.format(num),'{:>10}'.format(numBase2),'{:>5}'.format(numBase16)) #print numbers in base 10, 2 and 16. Give reasonable column widths for printing