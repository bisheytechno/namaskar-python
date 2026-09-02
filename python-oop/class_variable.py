# class variable = Shared among all instances of a class 
#                  Defined outside the constructor
#                  Allow you to share data among all objects from that class

class Student:

    class_year = 2027
    num_students = 0

    def __init__(self, name,age):
        self.name = name
        self.age  = age
        Student.num_students += 1


student1 = Student("Mike", 24)
student2 = Student("Spongebob", 34)
student3 = Student("Jonathan", 54)
student4 = Student("Lucas", 18)

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")


# print(student2.name)
# print(student2.age)
# print(Student.class_year)