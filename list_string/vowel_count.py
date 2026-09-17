# finding the vowels in a string
vowels = 'aeiouAEIOU'
check_string = input("Enter a string: ")
count = 0
if not check_string:
    print("The string is empty.")
    exit()
for char in check_string:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string is: {count}")