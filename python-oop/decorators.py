# # @property
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):               
        return self.__name


s = Student("Ram")
print(s.name)   


# @property + @setter

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    @property
    def name(self):              
        return self.__name

    @property
    def marks(self):             
        return self.__marks

    @marks.setter
    def marks(self, marks):       
        if marks < 0:
            print("❌ Negative hudaina!")
        elif marks > 100:
            print("❌ 100 bhanda badi hudaina!")
        else:
            self.__marks = marks
            print(f"✅ Marks updated: {marks}")

    def __str__(self):
        return f"{self.__name}: {self.__marks}"


s = Student("Ram", 85)


print(s.name)          
print(s.marks)         

s.marks = 95           
s.marks = -10          
s.marks = 150         
print(s)              

# @classmethod

class Student:
    total_students = 0            

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def get_total(cls):           
        return f"Total students: {cls.total_students}"


s1 = Student("Ram")
s2 = Student("Shyam")
s3 = Student("Hari")

print(Student.get_total())         

#  @staticmethod
class MathHelper:

    @staticmethod
    def add(a, b):                
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_even(n):
        return n % 2 == 0



print(MathHelper.add(5, 3))       
print(MathHelper.multiply(4, 5))  
print(MathHelper.is_even(10))      