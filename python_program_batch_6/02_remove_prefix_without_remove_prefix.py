# Ask user for input
user_input = input("Enter your text: ")
prefix_remover = input("Enter the prefix to terminate: ")

# Initiate a program that removes prefix manually
if user_input[:len(prefix_remover)] == prefix_remover:
    user_input = user_input[len(prefix_remover):]
    
# Print the result
print(user_input)