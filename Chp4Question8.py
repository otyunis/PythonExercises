#Author: Omar Yunis
#Date: March 4, 2021
#Description: Assignment 3 - Chapter 4 Question 8

num1 = 12
num2 = 12

#For integers between 1 and num1 and intgers between 1 and num2, generate all combinations of multiplications. Test the size of the number, allocate 3 spaces for numbers, if the number is less than 10, add two spaces in front, if less than 100 add one space in front, etc to keep the numbers aligned. Create a string out of each iteration of the inner loop, then print the line for each iteration of the outer loop
for i in range(num1):
    list = ''
    for j in range(num2):
        nextNum = (i+1)*(j+1)
        if nextNum < 10:
            nextNumStr = '  ' + str(nextNum)
        elif nextNum < 100:
            nextNumStr = ' ' + str(nextNum)
        else:
            nextNumStr = str(nextNum)
        list =  list + ' ' + nextNumStr
    print(list)