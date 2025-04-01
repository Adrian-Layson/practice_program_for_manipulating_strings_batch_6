# Ask user for input
user_input = input("Enter your text: ")

# Initialize 
result = ""

# Loop through every characters
for character in user_input:
    if "a" <= character <= "z":
        result += chr(ord(character) - 32)
    else:
        result += character

# Print the result
print(result)