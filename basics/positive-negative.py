#Getting the Postive and Negative numbers from the static num

num = -3
if num > 0:
    print("The number is Positive")
else:
    print("The number is Negative")

#fiding positive and negative numbers from the input method
getNum = int(input("Enter a number to check if it is positive or negative: "))
if getNum == 0:
    print("Please enter a number greater than 0 or less than 0")
elif getNum > 0:
    print(getNum, "is a Positive number")
else:
    print(getNum, "is a Negative number")