# variable = it is a resuable container for storing a value
#         a variable behaves as if it were the value it contains

#INTEGER

age = 21
players = 2
quantity = 5


print("You are " + age + "years old")
print("You are " , age , "years old")

print(f"You are ${age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")


# FLOAT

gpa = 3.6
distance = 5.6 
price = 10.99

print(f"Your gpa is ${gpa}")
print(f"You ran ${distance}")
print(f"The price is ${price}")


# STRING

name = "Mike"
food = "Bhuteko Bhat"
email = "brokxa123@gmail.com"


print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is : {email}")



# BOOLEAN

online = True
for_sale = False
running = True


print(f"Are you online? : {online}")
print(f"Is the item for sale? : {for_sale}")
print(f"Game running : {for_sale}")


if running: 
    print("The game is running")

else:
    print("The game is over")