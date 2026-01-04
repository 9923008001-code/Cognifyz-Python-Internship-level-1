def is_palindrome(text):
    # Convert to lowercase and remove spaces
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


# User input
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
