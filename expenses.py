expenses =[10.50, 8, 5, 15, 20, 5, 3]

#sum is to add each expense to as we loop over our list
sum = 0

for x in expenses:
    sum = sum + x
#sep = '' means you get rid of the space between the dollar sign and the total
print('You spent $', sum, ' on lunch this week', sep = '')

