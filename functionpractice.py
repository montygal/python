#Functions need to be declared first, at the top of the file
#Defining a function always starts with def
#The function name in this example is 'greeting'
#Directly next to the () in the function name goes the parameters
#The print statement needs to be indented
#Don't forget the colon

def greeting(name):
    print('Hello', name)

#Main program
input_name = input('Enter your name:\n')
greeting(input_name)

#In this example, the greeting
#function doesn't get used until it's called

#If we coded
#print('Thanks', name)
#we would receive an error
#because this is outside of the function