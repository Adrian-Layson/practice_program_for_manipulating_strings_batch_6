# Ask user for input
user_input = input("Enter your text: ")
width = int(input("Enter the width: "))

# If text is shorter than width, add spaces
if len(user_input) < width:
    result = " " * (width - len(user_input)) + user_input  
else:
    result = user_input

# Print the result