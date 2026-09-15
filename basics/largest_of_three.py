# Finding larget number from three numbers using if else statement
num1 = 10
num2 = 20
num3 = 30

if (num1 > num2) and (num1 > num3):
    print(f"{num1} is the largest number")
elif (num2 > num1) and (num2 > num3):
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")