# Ask user for input of both the string and suffix to check
user_input = input("Enter the text: ")
suffix = input("Enter the suffix to check: ")

# Checks if input ends with the entered suffix
if suffix == "":
    result = True
else:
    # Compare the end of the string
    result = user_input[-len(suffix):] == suffix

# Print the result
print(result)
