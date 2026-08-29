# Exercise 1.1. 

It is a good idea to read this book in front of a computer so you can try out the examples as you go

````Python
# print("Hello, World!")
````

# 1. In a print statement, what happens if you leave out one of the parentheses, or both?

````Python
print "Hello, World!" 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print ("Hello, World!" 
SyntaxError: '(' was never closed

print "Hello, World!" )
SyntaxError: unmatched ')'

prnt("Hello, World!")
SyntaxError: invalid syntax
````

# 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

````Python
print("Nikhil)
SyntaxError: unterminated string literal (detected at line 17)

print(Nikhil)
NameError: name 'Nikhil' is not defined

print("Nikhil")
````

# 3. You can use a minus sign to make a negative number like-2. What happens if you put a plus sign before a number? What about 2++2?

````Python
print(-2)

print(+-2)

print(2++2)
````

# 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?

````Python
print(011)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
````

# 5. What happens if you have two values with no operator between them?

````Python
print(2 2)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
````
