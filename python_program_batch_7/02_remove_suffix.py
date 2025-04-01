# Ask user for input and suffix to remove
user_input = input("Enter your text: ")
suffix_remover = input("Suffix to remove: ")

# Check if input ends with the suffix 
if user_input.endswith(suffix_remover):
    output = user_input[:-len(suffix_remover)] 
else:
    output = user_input

# Print
print(output)