# Ask user for input
user_input = input("Enter your text: ")

# Capitalize the first letter and lowercase the rest manually
if user_input:
    first_character = user_input[0].upper()
    rest_of_text = user_input[1:].lower()
    result = first_character + rest_of_text
else:
    result = ""

# Print the result