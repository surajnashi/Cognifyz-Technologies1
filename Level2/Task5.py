from collections import Counter

def count_word_occurrences(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Sort the word counts in alphabetical order
    sorted_word_counts = sorted(word_counts.items())

    # Display the results
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

# Provide the path to the text file
file_path = 'C:\Internship Task\Level2\Demo.txt'

# Call the function to count word occurrences
count_word_occurrences(file_path)
