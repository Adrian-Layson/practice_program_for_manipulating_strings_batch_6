# Ask user for input
user_input = input("Enter your text: ")

# Initialize value from the last character
start = len(user_input) - 1

# Loop until non-space character is found from right side
while start >= 0 and user_input[start] == " ":
    start -= 1

# Remove the substring
result = user_input[:start + 1]

# Print the result
print(result)