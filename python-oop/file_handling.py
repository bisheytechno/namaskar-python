# write file
with open("students.txt", "w") as file:
    file.write("Ram\n")
    file.write("Shyam\n")
    file.write("Hari\n")
print("✅ 3 students lekhiyo!")

#File padhau
print("\n📖 File padhau:")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

#append
with open("students.txt", "a") as file:
    file.write("Sita\n")
print("\n✅ One student added ")

#write
with open("myinfo.txt", "w") as file:
    file.write("Bishal\n")
    file.write("20\n")
    file.write("Lamahi\n")

print("This is my info")

#read
with open("myinfo.txt", "r") as file:
    for info in file:
        print(info.strip())

#append
with open("myinfo.txt", "a") as file:
    file.write("Python\n")

    print("Fav lang added")

#read 
with open("myinfo.txt", "r") as file:
    for info in file:
        print(info.strip())
