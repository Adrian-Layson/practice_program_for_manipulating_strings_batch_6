# Ask user for input and total width 
user_input = input("Enter the text: ")
width_input = int(input("Enter the total width: "))

# Center the text manually if width is greater than the inputted text
if width_input > len(user_input):
    extra_spaces = width_input - len(user_input)  
    left_spaces = extra_spaces // 2  
    right_spaces = extra_spaces - left_spaces  
    result = " " * left_spaces + user_input + " " * right_spaces
else:
    result = user_input

# Print the result
print(f"'{result}'")