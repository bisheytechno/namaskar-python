class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks < 0:
            print("❌ Negative marks hudaina!")
        elif marks > 100:
            print("❌ 100 bhanda badi hudaina!")
        else:
            self.__marks = marks
            print(f"✅ Marks updated: {marks}")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.__marks}")


s = Student("Ram", 85)

print(s.get_marks())      
s.set_marks(95)           
s.set_marks(-10)         
s.set_marks(150)          
s.display()


class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
            return self.__age

    def set_name(self,name):
         if name == "":
            print("Name can't be empty")
         else:
              self.__name = name
              print(f"Name updated : {name}")

    def set_age(self,age):
         if age < 0:
            print("Age can't be negative!")
         elif age > 150:
            print("Age 110 bhanda badi hudaina!")
         else:
            self.__age = age
            print(f"Age updated: {age}")

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")

p = Person("Ram", 25)
p.display()

print(p.get_name())   
print(p.get_age())    

p.set_name("Shyam")   
p.set_age(30)          

p.set_name("")        
p.set_age(-5)          
p.set_age(200)         

p.display()


class BankAccount:

    bank_name = "Nepal Bank"   

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):              
        return self.__owner

    def get_balance(self):
        return self.__balance

    def set_owner(self, owner):
        if owner == "":                    
            print("❌ Owner khali hudaina!")
        else:
            self.__owner = owner           
            print(f"✅ Owner updated: {owner}")

    def set_balance(self, balance):
        if balance < 0:                      
            print("❌ Balance negative hudaina!")
        else:
            self.__balance = balance          
            print(f"✅ Balance updated: {balance}")

    def display(self):
        print(f"\n🏧 {self.bank_name}")
        print(f"Owner   : {self.__owner}")
        print(f"Balance : Rs.{self.__balance}")
        print("-" * 25)


acc = BankAccount("Bishal", 1000000)
acc.display()

print(acc.get_owner())
print(acc.get_balance())

acc.set_owner("Radha")
acc.set_balance(200000000)    

acc.set_owner("")
acc.set_balance(-1000000)

acc.display()