# Author: Omar Yunis
# Date: Feb 18, 2021
# Assignment: Chapter 2 Exercise 13

# Problem statment: Based on the formula: V=(R+2E)/S, write a program that will
# calculate V based on user inputs of R (length of row in feet), E (amount of
# space used by end-post assembly in feet), and S (space between vines in feet)

# Request relevant values from user
rowLength_R = float(input('What is the length of the row (ft)?\n'))
endpostSpace_E = float(input('How much space is used by the end-post assembly (ft)?\n')) 
spaceBetween_S = float(input('How much space should be beteween vines (ft)?\n')) 

# Compute the number of vines that will fit in the row
numVines_V = (rowLength_R-2*endpostSpace_E)/spaceBetween_S

# Display the 'whole' number of vines that will fit
print(format(numVines_V,'.0f'),'vines will fit in the row.')
