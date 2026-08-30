name = "Bishal"

# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("l"))
# print(name.replace("l", "a"))
# print(name*3)



# 2nd example

# name = input("Enter your full name: ")

# result = len(name)

# result = name.find(" ")
# result = name.rfind("l")

# print(result)


# 3rd example
# validate user input exercise
# 1. username is no more than 12 char
# 2.username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")


if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"welcome {username}")