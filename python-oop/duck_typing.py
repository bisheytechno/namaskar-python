# class Dog:
#     def sound(self):
#         print("Woof!")

# class Cat:
#     def sound(self):
#         print("Meow!")

# class Human:
#     def sound(self):
#         print("Hello!")

# def make_sound(obj):
#     obj.sound()         

# sounds = [Dog(), Cat(), Human()]

# for living_being_sound in sounds:
#     living_being_sound.sound()


# ***Another Example***
class Animal:
    alive = True

class Dog(Animal):
    def sound(self):
        print("WOOF!")

class Cat(Animal):
    def sound(self):
        print("MEOW!")

class Bird():
    alive = False
    def sound(self):
        print("Flying!")


def make_sound(obj):
    obj.sound()           
    print(obj.alive)        


animals = [Dog(), Cat(), Bird()]

for animal in animals:
    make_sound(animal)      