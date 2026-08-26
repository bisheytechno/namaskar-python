# List =  [] ordered and changeable,Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK, NO Duplicates
# Tuple = () ordered and unchangeable, Duplicates OK. FASTER


# ----->>>> LIST

fruits = ["apple","orange","banana","coconut"]
print(dir(fruits))
print("apple" in fruits)
print(len(fruits))
print(fruits[::-1])
print(fruits[0:3])


fruits[0] = "pineapple"
print(fruits)

for fruit in fruits:
    print(fruit)

fruits.append("cherry")
print(fruits)

fruits.insert(1,"pineapple")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index("apple"))
print(fruits)



# ------->>>> SET


fruits = {"apple", "orange", "pineapple", "banana"}

print(fruits)
print(len(fruits))
print("pineapple" in fruits)
print("Cheery" in fruits)

fruits.add("mango")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()

fruits.clear()

print(fruits)



# -------->>>>> TUPLES


fruits = ("apple", "banana", "pineapple", "mango")

print(dir(fruits))


print(fruits.index("apple"))
print(fruits.count("pineapple"))
