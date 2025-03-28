# Ask user for input
user_input = input("Enter your text: ")

# Checker if all characters are in uppercase
is_uppercase = True
for char in user_input:
    if "a" <= char <= "z":
        is_uppercase = False
        break

# Print the result
print(is_uppercase)