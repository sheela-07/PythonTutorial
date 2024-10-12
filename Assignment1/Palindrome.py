def is_palindrome(word):
    """Function to check if a given word is a palindrome."""
    # Convert to lowercase and remove spaces
    word = word.lower().replace(" ", "")

    # Check if the word reads the same forwards and backwards
    return word == word[::-1]


# Input from user
word = input("Enter a word or phrase: ")

# Output the result
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
