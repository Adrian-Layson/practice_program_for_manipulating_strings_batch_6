# Ask user for input and character to find
user_input = input("Enter your text: ")
target_character = input("Enter the character to find: ")

# Find the first occurence of the character to find
char = user_input.find(target_character)

# Print the result
if char != 1:
    print(char)
else:
    print("Character not found")