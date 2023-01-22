#The first number is the start
#The second number is where it stops
#The third number is the step (or increments)
#range(2, 14, 2)
#output would be: 2, 4, 6, 8, 10, 12

total = 0
expenses = []
for i in range(7):
    expenses.append(float(input('Enter an expense:')))
total = sum(expenses)

print('You spent $', total, sep = '')
