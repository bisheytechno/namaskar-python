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