# Removing the duplicate elements

strName = "swiss"
unique = ""
for items in strName:
    # print(items)
    if items not in unique:
        unique += items
print("Unique characters:", unique)
