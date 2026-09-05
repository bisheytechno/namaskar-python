from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def sound(self):
        print("The dog is barking!")

    def move(self):
        print("The dog is running!")


class Bird(Animal):
    def sound(self):
        print("The bird is chirping!")

    def move(self):
        print("The bird is flying in the air!")


class Fish(Animal):
    def sound(self):
        print("The fish is silent...")

    def move(self):
        print("The fish is swimming under the water!")


animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.sound()
    animal.move()
    print("----------")