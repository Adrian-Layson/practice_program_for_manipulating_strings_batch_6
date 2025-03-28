# Ask user for input
user_input = input("Enter your text: ")

# Swap cases manually
result = ""
for char in user_input:
    if "A" <= char <= "Z":  
        result += chr(ord(char) + 32)
    elif "a" <= char <= "z":  
        result += chr(ord(char) - 32)
    else:
        result += char

# Print the result
print(result)