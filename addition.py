#Creating our addition function
def addition(a, b):
    return a + b

#Main program
num1 = float(input('Enter your 1st number:\n'))
num2 = float(input('Enter your 2nd number:\n'))

#Calling our function
result = addition(num1, num2)
print('The result is:', result)