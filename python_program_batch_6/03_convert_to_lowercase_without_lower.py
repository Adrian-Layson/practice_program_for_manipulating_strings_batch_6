# Ask user for input
user_input = input("Enter your text: ")

# Convert uppercase letters to lowercase manually
lowercase_output = ""
for char in user_input:
    if "A" <= char <= "Z":
        lowercase_output += chr(ord(char) + 32)
    else:
        lowercase_output += char

# Print the result
print(lowercase_output)