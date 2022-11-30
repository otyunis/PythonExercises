# Author: Omar Yunis
# Date: Feb 18, 2021
# Assignment: Chapter 2 Exercise 04

# Problem statement: A customer in a store is purchasing five items.
# Write a program that asks for the price of each item, and then displays 
# the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

# Get item prices from user
item1 = float(input('Enter the price of item 1 ($):\n'))
item2 = float(input('Enter the price of item 2 ($):\n'))
item3 = float(input('Enter the price of item 3 ($):\n'))
item4 = float(input('Enter the price of item 4 ($):\n'))
item5 = float(input('Enter the price of item 5 ($):\n'))

# Calculate subtotal, tax, and total based on specified tax rate
TAX_RATE = 0.07
subtotal = item1+item2+item3+item4+item5
salestax = subtotal*TAX_RATE
total = subtotal+salestax

# Display subtotal, tax, and total
print('Subtotal: $',format(subtotal, '.2f'),'\n',\
      'Tax: $',format(salestax, '.2f'), '\n',\
      'Total: $',format(total, '.2f'), sep=(''))
