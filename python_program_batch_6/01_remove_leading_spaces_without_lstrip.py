# Ask user for input
user_input = input("Enter your text: ")

# Initiate a program to remove leading spaces
for i in range(len(user_input)):
    if user_input[i] != " ":
        print(user_input[i:])
        break

# Print the result
else:
    print("No text entered. Try again.") 