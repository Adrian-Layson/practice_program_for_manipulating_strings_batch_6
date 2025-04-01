# Ask user for input and suffix to remove
user_input = input("Enter your text: ")
suffix_remover = input("Suffix to remove: ")

# Check if input ends with the suffix 
if user_input.endswith(suffix_remover):
    result = user_input[:-len(suffix_remover)] 
else:
    result = user_input

# Print the result
print(result)