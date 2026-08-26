# for loops -> execute a block of code a fixed number of times. iterate over range,string,sequence, etc.


credit_card = "1234-5678-9012-5678"

for x in credit_card:

    print(x)

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)


for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)



# ---------->while loop 

name  = input("Enter  your name:")

while name == "":
    print("You did not enter your name")
    name  = input("Enter  your name:")
    
print(f"Hello {name}")





age = int(input("Enter your age: "))

while age < 0 :
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")



food = input("Enter a food you like (q to quit) : ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit):")

print('bye')




num = int(input("Enter a # between 1 - 10 :"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 -10 :"))

print(f"your number is {num}")



# nested loop = A loop within another loop(outer,inner)
#                  outer loop:
#                    inner loop:



rows = int(input("Enter the number of rows: "))      
columns = int(input("Enter the number of columns: ")) 
symbol = input("Enter a symbol to use: ")             

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

