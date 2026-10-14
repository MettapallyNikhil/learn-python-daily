# Case Study

````Python
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
````
# Exercise 9.1. 
````Python
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
````
# Exercise 9.2

Write a program that reads words.txt and prints only the words that have no “e”. Compute the
percentage of words in the list that have no “e”.
````Python
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
````

# 9.3 Search
````Python
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
````
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?
````Python
from __future__ import print_function, division


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
````
