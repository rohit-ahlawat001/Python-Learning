#finnding the second largest number in the list using for loop

numbers = [3,5,7,2,7,1,9,4]
largeNum = numbers[0]
secondLarge = numbers[0]
for num in numbers:
    if num > largeNum:
        secondLarge = largeNum
        largeNum = num
    elif num > secondLarge and num != largeNum:
        secondLarge = num
print("The second largest number is:", secondLarge)