# Logical operators = used on conditional statements

# and = checks two or more conditions if True
# or = check if at least one condition is True
# not = True if condition is False, and vice-versa


#AND

temp = 25

if temp > 0 and temp < 30 :
    print("the temp is good")
else:
    print("the temp is not good")




#OR

temp = 40


if temp<=0 or temp >=30 :
    print("the temp is bad")
else:
    print("the temp is good")


#NOT

sunny = False

if not sunny:
    print("It is sunny outside")
else:
    print("It is cloudy outside")