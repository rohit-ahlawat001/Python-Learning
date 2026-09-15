# Checking the number even or the odd with the static number
num = 9
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Checking the number even or the odd with the user input
inputNum = int(input("Enter a number: "))
if inputNum == 0 or inputNum < 0:
    print(f"{inputNum} is neither even nor odd kindly enter a valid number")
elif inputNum % 2 == 0:
    print(f"{inputNum} is an even number")
else:
    print(f"{inputNum} is an odd number")

#finding the even and odd numbers in the list
numList = [1,2,3,4,5,6,7,8,9]
for num in numList:
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")