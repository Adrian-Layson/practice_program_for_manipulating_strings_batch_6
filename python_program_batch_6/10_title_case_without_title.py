# Ask user for input
user_input = input("Enter your text: ")

# Initialize the variables
result = ""
capitalize_char = True

# Loop through characters
for char in user_input:
    if char.isalpha():
        if capitalize_char:
            result += char.upper()
        else:
            result += char.lower()
        capitalize_char = False
    else:
        result += char
        capitalize_char = True

# Print the result
print(result)