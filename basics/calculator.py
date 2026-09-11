firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))
selectOperation = input("Select operation (+, -, *, /): ")

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