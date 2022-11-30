#Author: Omar Yunis
#Date: 04/28/2021
#Description: Assignment 5 - Chapter 6 - Exercise 12

months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug', 'Sep','Oct','Nov','Dec') #months in order
daysInMonths = (31,28,31,30,31,30,31,31,30,31,30,31) #days in months in order

fname = 'steps.txt' #file name with steps
with open(fname,'r') as file: #open file using context manager
    lines = file.readlines() #read all lines from file into list (elements are strings)
    print("{: <5} | {: >10}".format('Month','Avg. Steps')) #add column headers
    for i in range(0,len(months)): #iterate over each month
        leftIdx = sum(daysInMonths[0:i]) #calculate starting index
        rightIdx = sum(daysInMonths[0:i+1]) #calculate ending index
        linesInMonth = [int(line.replace('\n','')) for line in lines[leftIdx:rightIdx]] #get lines based on start and end indexes, delete new line characters, convert to integers, and store in list
        totalStepsInMonth = sum(linesInMonth) #sum up all steps
        avgStepsInMonth = round(totalStepsInMonth/daysInMonths[i]) #calculate average by dividing total steps by number of days in month
        print("{: ^5} | {: ^10}".format(months[i],avgStepsInMonth)) #display result in columns
