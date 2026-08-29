# if = do some code only IF some condition is True
#     Else do something else


# 1st example

age = int(input("Enter your age: "))

if age >= 18:
    print("You can signup")
elif age < 0:
    print("You haven't been born yet!")

elif age >=100:
    print("You are too old to signup")
else:
    print("You can't signup")


# 2nd example

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")

else:
    print("No food for you!")


# 3rd example

name = input("Enter your name :")

if name == "":
    print("You did not type in your name")

else:
    print(f" Hello {name}")


# 4th example

for_sale = True

if for_sale:
    print("This item  is for sale")
else:
    print("This item is not for")