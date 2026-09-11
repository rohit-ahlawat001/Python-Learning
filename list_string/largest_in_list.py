lst = [3,5,7,2,7,1,9,4]

# Finding the largest number in the list using built-in function
lagestNum = max(lst)
print("The largest number in the list is: ", lagestNum)


# Finding the largest number in the list using for loop

largeNum = lst[0]
for num in lst:
    if num > largeNum:
        largeNum = num
print("The largest number in the list is: ", largeNum)