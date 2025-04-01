# Ask user for input and text to be counted
user_input = input("Enter your text: ")
text_counter = input("Enter the text to count: ")

# Initialize
text = 0
count = 0

# Loop through every characters
while text <= len(user_input) - len(text_counter):
    if user_input[text : text + len(text_counter)] == text_counter:
        count += 1
    text += 1

# Print the result
print(count)