# class InvalidException(Exception):
#     # pass #placeholder for future code, not implemented yet
#     def __init__(self, message, errors):
#         super().__init__(message) #proxy object (temporary object of the super class) that allows us to access methods of the base class
#         self.errors = errors
    

# number = input("Enter a number:\n")

# try:
#     if not number.isnumeric():
#         raise InvalidException("Error, numeric was not entered", "Error")
#     else:
#         print("Number entered: ", number)

# except InvalidException as e:    
#     print(e)    


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return (repr(self.value)) #repr returns a printable representation of the given object

try:
    raise(MyError(3*2))
except MyError as error:
    print('Exception thrown: ', error.value)
finally:
    print('Ending program')