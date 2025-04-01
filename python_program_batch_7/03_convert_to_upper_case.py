# Ask user for input
user_input = input("Enter your text: ")

# Initialize 
output = ""

# Loop through every characters
for character in user_input:
    if "a" <= character <= "z":
        output += chr(ord(character) - 32)
    else:
        output += character

# Print
print(output)