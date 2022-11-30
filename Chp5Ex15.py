#Author: Omar Yunis
#Date: 04/16/2021
#Description: Assignment 4 - Chapter 5 - Exercise 15

#MAIN
def main():
    grades = []
    for i in range(1,5+1):
        grade = float(input('Enter your grade for test {}: \n'.format(i)))
        grades.append(grade)
    average = calc_average(grades)
    letterGrades = determine_grade(grades)
    print('Your test grades are:\n',grades)
    print('Your corresponding letter grades are:\n',letterGrades)
    print('Your average is: {:.2f}%'.format(average))
    

#FUNCTIONS
def calc_average(grades):
    total = 0
    for grade in grades:
        total = total + grade
    avg = total/len(grades)
    return avg

def determine_grade(grades):
    letterGrades = []
    for grade in grades:
        if grade < 60:
            letter = 'F'
        elif grade < 70:
            letter = 'D'
        elif grade < 80:
            letter = 'C'
        elif grade < 90:
            letter = 'B'
        else:
            letter = 'A'
        letterGrades.append(letter)
    return letterGrades

if __name__ == '__main__':
    main()
