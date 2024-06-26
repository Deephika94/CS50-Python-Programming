string = input("Input:")
output = ""
for letter in string:
    if letter.lower() in ['a','e','i','o','u']:
        continue
    else:
        output = output + letter
print(output)
