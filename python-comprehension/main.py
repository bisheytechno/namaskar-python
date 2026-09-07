# without comprehension is long

sqaure = []

for i in range(1,11):
    sqaure.append(i ** 2)

print(sqaure)


# with comprehension in list

squares = [i ** 2 for i in range(1, 11)]
print(squares)


# >>>>>>>>>>>>>>LIST EXAMPLE WITH COMPREHENSION>>>>>>>
#double
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)    

#compare

evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)    

#upper
fruits = ["apple", "banana", "mango"]
upper = [f.upper() for f in fruits]
print(upper)     

#food name print letter more than 5 char
long_fruits = [f for f in fruits if len(f) > 5]
print(long_fruits)  



# >>>>>>>>>>>>>>DICT EXAMPLE WITH COMPREHENSION>>>>>>>



squares = {i: i ** 2 for i in range(1, 6)}
print(squares)




students = ["Ram", "Shyam", "Hari"]
marks = [85, 92, 78]

result = {s: m for s, m in zip(students, marks)}
print(result)


# >>>>>>>>>>>>>>SET EXAMPLE WITH COMPREHENSION>>>>>>>

numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {n ** 2 for n in numbers}
print(unique_squares)
