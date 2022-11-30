#Author: Omar Yunis
#Date: Mar 4, 2021
#Description: Assignment 2 - Chapter 3 Exercise 12


PACKAGE_PRICE = 99 #dollars per package

#discount rates for different package ranges (converted from % to decimal)
DISC_10_TO_19 = 0.1
DISC_20_TO_49 = 0.2
DISC_50_TO_99 = 0.3
DISC_OVER_100 = 0.4

#get the number of packages that the user purchased
numPacks = int(input('How many packages did you purchase?'))

#calculate the total before discount
priceB4Discount = numPacks*PACKAGE_PRICE

#for each range, calculate the discount, the discounted total, and display to user
if 0 <= numPacks <= 9:
    discount = 0
    total = priceB4Discount
    print('Discount: $',discount,'\n' ,'Discounted Total: $',total, sep='')
elif 10 <= numPacks <= 19:
    discount = DISC_10_TO_19*priceB4Discount
    total = priceB4Discount - discount
    print('Discount: $',discount,'\n' ,'Discounted Total: $',total, sep='')
elif 20 <= numPacks <= 49:
    discount = DISC_20_TO_49*priceB4Discount
    total = priceB4Discount - discount
    print('Discount: $',discount,'\n' ,'Discounted Total: $',total, sep='')
elif 50 <= numPacks <= 99:
    discount = DISC_50_TO_99*priceB4Discount
    total = priceB4Discount - discount
    print('Discount: $',discount,'\n' ,'Discounted Total: $',total, sep='')
elif numPacks >= 100:
    discount = DISC_OVER_100*priceB4Discount
    total = priceB4Discount - discount
    print('Discount: $',discount,'\n' ,'Discounted Total: $',total, sep='')
else:
    print('You did not enter a valid input.')