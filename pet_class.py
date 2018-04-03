class Pet:
    """ This is the beginning of a class for the superior dog.
            Attributes:
            name
            weight
            
"""
    foodDishLevel = 100
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        Dog.foodDishLevel -= 10

class Dog(Pet):
    """ Dog inherits from Pet"""

class Cat(Pet):
    """ Cat inherits from Pet"""

c = Dog('Fido')


x = Cat('Fluffy')


x.add_weight(12)


print(c.name)

print(x.name)
print(x.weight)

x.eat
print(c.foodDishLevel)
print(x.foodDishLevel)

