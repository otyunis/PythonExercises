#Author: Omar Yunis
#Date: March 4, 2021
#Description: Assignment 3 - Chapter 4 Exercise 14

#Initialize the size of the triangle
size = 7

#While the size is greater than 0, make a string of consecutive '*' and print. Decrement size by 1 each loop.
while size > 0 :
    string = ''
    for s in range(size):
        string = string + '*'
    print(string)
    size = size - 1