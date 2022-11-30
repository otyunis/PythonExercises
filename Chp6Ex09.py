#Author: Omar Yunis
#Date: 04/28/2020
#Description: Assignment 5 - Chapter 6 - Exercise 06

#Set proper directory first
def avgFromTxt(fname): #pass file name as argument
    try:
        with open(fname,'r') as file: #open file for reading
            counter = 0
            total = 0
            for num in file:
                counter += 1 #count number of numbers
                total = total + int(num) #sum all numbers
            avg = total/counter #calculate average
        return {'total':total, '# elements':counter, 'average':avg}
    except IOError: #if trouble with opening file
        print('IO Error Occured')
    except ValueError: #if trouble with contents of file
        print('Value Error Occured')
print('Average: ',avgFromTxt('numbers.txt')['average'])
    