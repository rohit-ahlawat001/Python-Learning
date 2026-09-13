# Check if a number is even or odd using the static method
checkNum = 5
if checkNum % 2 == 0:
    print(checkNum, "is an even number")    
else:
    print(checkNum, "is an odd number")


#check if a number is even or odd using the inut method
getNum = int(input("Enter a number to check if it is even or odd: "))

if getNum == 0:
    print("Please enter a number greater than 0")
elif getNum % 2 == 0:
    print(getNum, "is an even number")
else:
    print(getNum, "is an odd number")