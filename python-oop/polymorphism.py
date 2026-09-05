# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass


# class Dog(Animal):
#     def sound(self):
#         print("The dog is barking!")

#     def move(self):
#         print("The dog is running!")


# class Bird(Animal):
#     def sound(self):
#         print("The bird is chirping!")

#     def move(self):
#         print("The bird is flying in the air!")


# class Fish(Animal):
#     def sound(self):
#         print("The fish is silent...")

#     def move(self):
#         print("The fish is swimming under the water!")


# animals = [Dog(), Bird(), Fish()]

# for animal in animals:
#     animal.sound()
#     animal.move()
#     print("----------")



# *****--Another example---------**

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
       self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
      self.side = side

    def area(self):
        return self.side **2

class Rectangle(Shape):
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

shapes = [Circle(4), Square(3), Rectangle(5,5)]

for shape in shapes:
    print(shape.area())