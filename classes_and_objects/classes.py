class Robot_Dog:
    #self is the first parameter in a init method
    #same thing a this
    #refers to the instance of the class that we are creating    
    #other parameters are ones we want to initalize
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    #self is always needed in class methods
    #self is an instance of a class - an object
    def bark(self):
        print("Woof!")

my_dog = Robot_Dog('Remi', 'Dachshund')
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()