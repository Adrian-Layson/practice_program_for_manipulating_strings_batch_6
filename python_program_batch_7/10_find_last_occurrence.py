# Ask user for input and charactert to find
user_input = input("Enter your text: ")
target_character = input("Enter the character to find: ")

# Loop through the string from the end
for char in range(len(user_input) -1, -1, -1):
    if user_input[char] == target_character:
        # Print the result
        print(char) 
        break
else:
    print("Character not found")