firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))
selectOperation = input("Select operation (+, -, *, /): ")

if (firstNum == 0 or secondNum == 0) and (selectOperation == "/" or selectOperation == "*"):
    print("Please enter a number greater than 0")

if selectOperation == "+":
    result = firstNum + secondNum
    print("The result is: ", result)
elif selectOperation == "-":
    result = firstNum - secondNum
    print("The result is: ", result)
elif selectOperation == "*":
    result = firstNum * secondNum
    print("The result is: ", result)
elif selectOperation == "/":
        result = firstNum / secondNum
        print("The result is: ", result)