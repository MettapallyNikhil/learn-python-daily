# Write a program that reads a file, breaks each line into words, strips whitespace and
# counts the frequency of each word. The program should then print the top 10 most frequent words along with 
# their counts.

from collections import Counter 

def count_word_frequency(file_path):
    # Initialize a Counter to hold word frequencies
    word_count = Counter()

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words, strip whitespace, and update the counter
            words = line.split()
            stripped_words = [word.strip() for word in words]
            word_count.update(stripped_words)

    # Get the top 10 most common words
    top_words = word_count.most_common(10)

    # Print the top 10 words with their counts
    print("Top 10 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")  

# Example usage
if __name__ == "__main__":
    file_path = 'C:\\Users\\Hp\\PythonLearning\\words.txt'  # Replace with your file path
    count_word_frequency(file_path)