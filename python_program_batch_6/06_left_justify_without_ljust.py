# Ask user for the input and total width
user_input = input("Enter the text: ")
width_input = int(input("Enter the total width: "))

# Check if text meets the exact width
if len(user_input) < width_input:
    result = user_input + " " * (width_input - len(user_input))
else:
    result = user_input

# Print the result
print(f"'{result}'")