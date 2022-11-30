#Author: Omar Yunis
#Date: 04/16/2021
#Description: Assignment 4 - Chapter 5 - Exercise 13

#MAIN
def main():
    for i in range(1,10+1):
        d = falling_distance(i)
        print('For t = {} [s], d = {:.2f} [m]'.format(i,d))

#FUNCTIONS
def falling_distance(fall_time):
    g = 9.8
    d = 0.5*g*fall_time**2
    return d

if __name__ == '__main__':
    main()
