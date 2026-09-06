 #__str__
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student : {self.name} , Marks : {self.marks}"

s = Student("Ram", 98)
print(s)

#__len__
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


p = Playlist(["Song1", "Song2", "Song3"])
print(len(p)) 
 
        
#__add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2        
print(v3) 

      
# __gt__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):       
        return self.marks > other.marks

    def __str__(self):
        return f"{self.name}: {self.marks}"


s1 = Student("Ram", 85)
s2 = Student("Shyam", 92)

print(s1 > s2)    
print(s2 > s1)   


if s1 > s2:
    print(f"{s1} won!")
else:
    print(f"{s2} won!")


#__eq__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks   

    def __str__(self):
        return f"{self.name}: {self.marks}"


s1 = Student("Ram", 85)
s2 = Student("Shyam", 85)
s3 = Student("Hari", 90)

print(s1 == s2)    
print(s1 == s3)  

if s1 == s2:
    print(f"{s1} ra {s2} ko marks same xa!")
else:
    print("Marks alag xa!")

