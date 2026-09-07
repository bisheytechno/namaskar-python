try:
    number  = int(input("Enter a number :"))
    result = 100/number

except ValueError:
    print("Give only number not string!")

except ZeroDivisionError:
    print("It is not divisible by zero!")

else:
    print(f"The result is : {result}")

finally:
    print("Thank you sir !")