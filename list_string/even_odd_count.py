# Checking the number even or the odd with the static number
num = 9
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Checking the number even or the odd with the user input
inputNum = int(input("Enter a number: "))
if inputNum == 0:
    print(f"{inputNum} is neither even nor odd")
elif inputNum % 2 == 0:
    print(f"{inputNum} is an even number")
else:
    print(f"{inputNum} is an odd number")