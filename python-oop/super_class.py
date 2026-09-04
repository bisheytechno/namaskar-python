# super() = Function used in ina achild class to call method from a parent class(superclass).
# allows you to extend the functionality of the inherited methods

class Animal:
    def __init__(self, name,color, age):
        self.name = name
        self.age = age
        self.color = color
        print(f"Animal name is : {name}")

    def describe(self):
        print(f"It is {self.color} animal.")


class Dog(Animal):
    def __init__(self, name,color, age, breed):
        super().__init__(name,color, age)  
        self.breed = breed          
        print(f"Dog breed: {breed}")


d = Dog("Bruno", "red" , 3,"Labrador")
d.describe()

print(d.name)  
print(d.age)   
print(d.breed)  


# multilevel inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"1. Animal: {name} banyo!")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  
#         self.breed = breed
#         print(f"2. Dog: {breed} breed!")


# class Puppy(Dog):
#     def __init__(self, name, breed, age):
#         super().__init__(name, breed)  
#         self.age = age
#         print(f"3. Puppy: {age} months!")


# p = Puppy("Bruno", "Labrador", 3)


# print(p.name)   
# print(p.breed)  
# print(p.age)    