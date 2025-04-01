# Ask user for input and desired width
user_input = input("Enter your text: ")
width = int(input("Enter the width: "))

# Add zero if text is shorter than width
if len(user_input) < width:
    result = "0" * (width - len(user_input)) + user_input
else:
    result = user_input

# Print the result
print(result)