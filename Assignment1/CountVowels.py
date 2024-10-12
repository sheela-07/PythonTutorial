def count_vowels_consonants(word):
    """Function to count vowels and consonants in a word."""
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    # Convert to lowercase to ignore case
    word = word.lower()

    # Iterate through each character in the word
    for char in word:
        if char.isalpha():  # Check if the character is alphabetic
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Input from user
word = input("Enter a word: ")

# Output the vowel and consonant count
vowel_count, consonant_count = count_vowels_consonants(word)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
