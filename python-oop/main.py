# object = a "bundle" of related attributes(variables) and methods(functios) Ex. Phone, cup, book
#         you need a "class" to create many objects


# class = (blueprint) used to design the structure and layout of an object
from car import Car


car1 = Car("BMW", 2024, "black", False)
car2 = Car("Mustang", 2025, "red", True)

car1.drive()
car1.stop()
car2.drive()
car1.describe()