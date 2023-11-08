#order matters for functions. Must be defined before we can use it
#scope matters as well
#name only exists in the function


# def greeting(name):
#     print('Hello', name)


# input_name = input("Enter Name: ")

# greeting(input_name)

#using global scope for variable name
#this is messy, only should be used for constants

def greeting():
    print('Hello', name)

name = input('Enter Name: ')
greeting()