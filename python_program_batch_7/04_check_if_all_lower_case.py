# Ask user for input
user_input = input("Enter your text: ")

# Initialize the checker
if_lower = True

# Loop through every characters
for character in user_input:
    if "A" <= character <= "Z":
        if_lower = False
        break


# Print the result
print(if_lower)
