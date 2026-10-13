# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)

# Exercise 9.1. 

# Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace).

# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     if len(word) > 20:
#         print(word)

# Exercise 9.2

# Write a program that reads words.txt and prints only the words that have no “e”. Compute the
# percentage of words in the list that have no “e”.

fin = open('words.txt')
count = 0
total = 0
for line in fin:
    word = line.strip()
    total += 1
    if 'e' not in word:
        print(word)
        count += 1

print(f"Percentage of words without 'e': {count/total*100:.2f}%")