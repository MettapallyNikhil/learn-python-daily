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
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
````Python
import datetime
initial_leaving_house = datetime.datetime(2026, 1, 1, 6, 52)
mile_at_an_easy_pace = datetime.timedelta(minutes=8, seconds=15)
mile_at_tempo = datetime.timedelta(minutes=7, seconds=12)
total_running_time = (
    mile_at_an_easy_pace
    + (mile_at_tempo * 3)
    + mile_at_an_easy_pace
)
arrival_time = initial_leaving_house + total_running_time
print(arrival_time.strftime("%I:%M:%S %p"))
````
# Exercises 3.1.

# Write a function named right_justify that takes a string named as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display. 
right_justify('monty') Hint: Use string concatenation and repetition. Also, Python provides a built-in function called lenthat returns the length of a string, so the value of len('monty') is 5

````Python
def right_justify(s):
    print(' ' * (70 - len(s)) + s)
right_justify('monty')
````
# Adding new Function

`````Python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()
repeat_lyrics()
``````
# Inside a function, the arguments are assigned to the variable called Parameters
`````Python
def print_thrice(bruce):
    print(bruce)
    print(bruce)
    print(bruce)

print_thrice('Spam')
print_thrice('Nikhil')
print_thrice(math.pi)

print_thrice('Hello, World!'*10)
``````
# We can use variable as an argument to a function. The value of the variable is assigned to the parameter.
`````Python
Micheal = "Nikhil & Snehal"
print_thrice(Micheal)

# Variables and parameters are local

def cat_twice(part1, part2, part3):
    # Concatenates three strings and prints them three times.
    cat = part1 + part2 + part3
    print_thrice(cat)

a = 'Bing'
b = 'Bong'
c = 'Bung'
cat_twice(a, b, c)
``````

# I am using the script mode, untill and unless i say print it wont print
`````Python
math.sqrt(10)
print(math.sqrt(10))
``````

# Exercise 3.2. 

# A function object is a value you can assign to a variable or pass as an argument.For example, do_twice is a function that takes a function object as an argument and calls it twice:
`````Python
def do_twice(f):
    f()
    f()
``````
# Here’s an example that uses do_twice to call a function named print_spam twice.
`````Python
def print_spam():
    print('spam')
``````  
do_twice(print_spam)

# 1. Type this example into a script and test it.
`````Python
do_twice(print_spam)
``````
# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
`````Python
def do_twice(f, value):
    f(value) #function object
    f(value)
``````
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
`````Python
def print_twice(bruce):
    print(bruce)
    print(bruce)
``````
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
`````Python
do_twice(print_twice, 'spam')
``````
# 5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
`````Python
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
``````
# Case study: interface design

4.1 The turtle module making an square

`````Python
import turtle
bob = turtle.Turtle()
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
print(bob)
turtle.mainloop()
``````
# 4.2 Simple repetition 

`````Python
for i in range(4):
    print('Hello!')
``````
# Drawing a square using a for loop
`````Python
import turtle
bob = turtle.Turtle()
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()
``````
