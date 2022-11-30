#Author: Omar Yunis
#Date: Mar 4, 2021
#Description: Assignment 2 - Chapter 3 Exercise 18

#Get user input about dietary restrictions
vegetarianYorN = input('Is anyone in your party vegetarian (yes/no)?\n')
veganYorN = input('Is anyone in your party vegan (yes/no)?\n')
glutenfreeYorN =input('Is anyone in your party gluten-free (yes/no)?\n')

#Assign the restaurant names to string variables
JGB = "Joe's Gourmet Burgers"
MSPC = "Main Street Pizza Company"
CC = "Corner Cafe"
MFI = "Mama's Fine Italian"
TCK = "The Chef's Kitchen"

#If the party has a particular dietary restriction, delete the correpsonding 
#restaurant by setting the variable to the empty string (so it isn't displayed)
if vegetarianYorN == 'yes':
    JBG = ""
if veganYorN == 'yes':
    JBG = ""
    MSPC = ""
    MFI = ""
if glutenfreeYorN == 'yes':
    JGB = ""
    MFI = ""

#Display the resulting (non-deleted) restaurants to the user
print("Your options are:\n",JGB,'\n',MSPC,'\n',CC,'\n',MFI,'\n',TCK,'\n')