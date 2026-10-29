# # Write a program that reads a file, breaks each line into words, strips whitespace and
# # counts the frequency of each word. The program should then print the top 10 most frequent words along with 
# # their counts.

# from collections import Counter 

# def count_word_frequency(file_path):
#     # Initialize a Counter to hold word frequencies
#     word_count = Counter()

#     # Open the file and read line by line
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Split the line into words, strip whitespace, and update the counter
#             words = line.split()
#             stripped_words = [word.strip() for word in words]
#             word_count.update(stripped_words)

#     # Get the top 10 most common words
#     top_words = word_count.most_common(10)

#     # Print the top 10 words with their counts
#     print("Top 10 most frequent words:")
#     for word, count in top_words:
#         print(f"{word}: {count}")  

# # Example usage
# if __name__ == "__main__":
#     file_path = 'C:\\Users\\Hp\\PythonLearning\\words.txt'  # Replace with your file path
#     count_word_frequency(file_path)

# # Modify your program from the previous exercise to read the book you downloaded, skip over the
# # header information at the beginning of the file, and process the rest of the words as before.


# from collections import Counter

# def count_word_frequency(file_path):
#     word_count = Counter()
#     total_words = 0

#     with open(file_path, "r", encoding="utf-8") as file:
#         # Skip the header
#         for line in file:
#             if line.strip().startswith("*** START OF"):
#                 break
#         else:
#             print("Start marker not found in the file.")
#             return

#         # Count words after the header
#         for line in file:
#             words = line.lower().split()
#             word_count.update(words)
#             total_words += len(words)

#     print(f"Total number of words: {total_words}")
#     print("Top 10 most frequent words:")

#     for word, count in word_count.most_common(10):
#         print(f"{word}: {count}")


# if __name__ == "__main__":
#     file_path = r"C:\Users\Hp\PythonLearning\Sherlock holmes.txt"
#     count_word_frequency(file_path)

# # Random numbers

# import random
# for i in range(10):
#     x = random.random()

# print(x)

# t = [1, 2, 3, 4, 5]
# random.shuffle(t)

# print(t)

# # Write a function named choose_from_hist that takes a histogram as defined in
# # Section 11.2 and returns a random value from the histogram, chosen with probability in proportion
# # to frequency. 

# def choose_from_hist(hist):
#     total = sum(hist.values())
#     rand_val = random.uniform(0, total)
#     cumulative = 0

#     for key, freq in hist.items():
#         cumulative += freq
#         if rand_val < cumulative:
#             return key

# # Example usage
# print(choose_from_hist({'a': 5, 'b': 2, 'c': 3}))
# print(choose_from_hist({'apple': 10, 'banana': 5, 'cherry': 15}))

#  Word histogram

# import string

# def process_file(filename):
#     hist = {}
#     with open(filename, 'r', encoding='utf-8') as fp:
#         for line in fp:
#             process_line(line, hist)
#     return hist

# def process_line(line, hist):
#     line = line.replace('-', ' ')
#     for word in line.split():
#         word = word.strip(string.punctuation + string.whitespace)
#         word = word.lower()
#         if word:  # Skip empty strings
#             hist[word] = hist.get(word, 0) + 1

# hist = process_file('Sherlock holmes.txt')
# print(hist)

# Most common words


import string


def process_file(filename):
    hist = {}

    with open(filename, 'r', encoding='utf-8') as fp:
        for line in fp:
            process_line(line, hist)

    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        if word:
            hist[word] = hist.get(word, 0) + 1


def most_common(hist, excluding_stopwords=False):
    stopwords = {
        'the', 'and', 'to', 'of', 'a', 'in', 'that', 'is', 'it', 'for',
        'on', 'with', 'as', 'was', 'at', 'by', 'an', 'be', 'this', 'which',
        'or', 'from', 'but', 'not', 'are', 'have', 'has'
    }

    if excluding_stopwords:
        filtered_hist = {
            word: count
            for word, count in hist.items()
            if word not in stopwords
        }
    else:
        filtered_hist = hist

    return sorted(
        filtered_hist.items(),
        key=lambda item: item[1],
        reverse=True
    )[:10]


# Execute the program
hist = process_file('Sherlock holmes.txt')

print("Top 10 words excluding stopwords:")
print(most_common(hist, excluding_stopwords=True))

print("\nTop 10 words including stopwords:")
print(most_common(hist, excluding_stopwords=False))
