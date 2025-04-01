# Ask user for input and prefix to check
user_input = input("Enter a text: ")
prefix_check = input("Enter the prefix to be checked: ")

# Check prefix
if not prefix_check:
    result = True
else:
    # Remove first part of input and compare to prefix
    result = user_input[:len(prefix_check)] == prefix_check 

# Print the result
print(result)