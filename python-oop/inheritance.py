# Inheritance = Allows a class to inherit attributes and methods from another class
#               helps with code resuability and extensibility
#               class Child (Parent)


class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

class Snake(Animal):
    def speak(self):
        print("Hisshh!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")
snake = Snake("Robin")

dog.speak()
print(cat.is_alive)
cat.eat()
cat.sleep()
snake.eat()