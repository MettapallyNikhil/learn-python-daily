# Exercise 1.1. 

It is a good idea to read this book in front of a computer so you can try out the examples as you go

````Python
print("Hello, World!")
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

# Exercise 1.2. Start the Python interpreter and use it as a calculator.

# 1. How many seconds are there in 42 minutes 42 seconds?

````Python
a = 42
b = 60
c = 42
d = (a*b+c)
print(d)
````
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

````Python
e = 1.61
f = 10
g = (f/e)
print(g)
````
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? 

````Python
h = (d/g) # time in secs
print(h)
i = (h/60) # in minutes
print(i)
````

# What is your average speed in miles per hour?
````Python
j = (g/d*3600)
print(j)
````

# Exercise 2.1

Repeating my advice from the previous chapter, whenever you learn a new feature, you should try it out in interactive mode and make errors on purpose to see what goes wrong.

# We’ve seen that n = 42 is legal. What about 42 = n?

````Python
n = 42
42 = n # SyntaxError: cannot assign to literal
````

# Howabout x = y = 1?

````Python
x = y = 1
````

# In some languages every statement ends with a semi-colon ;. What happens if you put a semi-colon at the end of a Python statement?

````Python
if; #SyntaxError: invalid syntax
````

# What if you put a period at the end of a statement?

````Python
if. #SyntaxError: invalid syntax
````
# In math notation you can multiply x and y like this: xy. What happens if you try that in Python?

````Python
x = 2
y = 3
print(xy) # NameError: name 'xy' is not defined
````
# Exercise 2.2 Practice using the Python interpreter as a calculator:

# 1. The volume of a sphere with radius r is 4/3πr3. What is the volume of a sphere with radius 5?
````Python
r = 5
volume = (4/3)*3.14159*(r**3)
print(volume)
````
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
````Python
cover_price_of_a_book = 24.95
discount = 0.4
shipping_costs_for_the_first_copy = 3
shipping_costs_for_additional_copies = 0.75
wholesale_cost = cover_price_of_a_book * (1 - discount) * 60 + shipping_costs_for_the_first_copy 
+ shipping_costs_for_additional_copies * (60 - 1)
print(wholesale_cost)
````
