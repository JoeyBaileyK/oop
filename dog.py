class Dog:
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
        Cat.foodDishLevel -= 10


c = Dog('Fido')
# c.name = "Fido"

x = Dog('Rufus')
# x.name = "Rufus"

x.add_weight(12)
# x.add_wieght(12)

print(c.name)

print(x.name)
print(x.weight)

x.eat()
print(c.foodDishLevel)
print(x.foodDishLevel)
