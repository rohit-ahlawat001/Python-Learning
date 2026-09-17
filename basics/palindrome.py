string = str(input("Enter a string: "))  
new_string = string[::-1]
if string == new_string:
    print(f"{string} is a palindrome.")