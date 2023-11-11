from parent_class import Robot


class Robot_Dog(Robot):    
    def make_noise(self):
        print('Woof')

    def eat(self):
        print('Eating from child class')