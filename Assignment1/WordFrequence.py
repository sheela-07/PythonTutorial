import string


def word_frequency(sentence):
    """Function to calculate the frequency of words in a sentence."""
    # Convert to lowercase and remove punctuation
    sentence = sentence.lower().translate(str.maketrans("", "", string.punctuation))

    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store word frequencies
    frequency_dict = {}

    # Count the frequency of each word
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict


# Input from user
sentence = input("Enter a sentence: ")

# Output the word frequency
print(word_frequency(sentence))
