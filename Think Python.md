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
# 4.3 Exercises - using the turtle module.

# 1. Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square. Write a function call that passes bob as an argument to square, and then run the program again.

`````Python
import turtle
bob = turtle.Turtle()
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(bob) 
turtle.mainloop()
``````
# 2. Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for length.
`````Python
import turtle
bob = turtle.Turtle()
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
square(bob, -150) 
turtle.mainloop()
``````
# 3. Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
`````Python
import turtle
bob = turtle.Turtle()
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
polygon(bob, 150, 5) 
turtle.mainloop()
``````
# 4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle by calling polygon with an appropriate length and number of sides. Test your function with a range of values of r. Hint: figure out the circumference of the circle and make sure that length * n = circumference.
`````Python
import turtle
bob = turtle.Turtle()
def circle(t, r):
    # Calculate the number of sides for the polygon
    n = 25
    # Calculate the length of each side
    length = 2 * r * 3.14159 / n
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
circle(bob, 100) 
turtle.mainloop()
``````
# 5. Make a more general version of circle called arc that takes an additional parameter angle, which determines what fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.
`````Python
import turtle
bob = turtle.Turtle()
def arc(t, r, angle):
     # Calculate the number of sides for the polygon
     n = 100
     # Calculate the length of each side
     length = 2 * r * 3.14159 / n
     # Calculate the angle of each turn
     turn_angle = 360 / n
     # Draw the arc
     for i in range(int(angle / turn_angle)):
         t.fd(length)
         t.lt(turn_angle)

 arc(bob, 100, 180)
 turtle.mainloop()
``````
# 6. Polyline
`````Python
import turtle
bob = turtle.Turtle()

def polyline(t, n, length, angle):
     """Draws n line segments with the given length and angle between them."""
     for i in range(n):
         t.fd(length)
         t.lt(angle)

polyline(bob, 100, 180, 180)
turtle.mainloop()
``````
# Exercise 4.4. 

# 1. Draw a stack diagram that shows the state of the program while executing circle(bob,radius). You can do the arithmetic by hand or add print statements to the code.
`````Python
import turtle
import math
bob = turtle.Turtle()

def polygon(t, length, n):
    print("---- POLYGON FRAME ----")
    print("t =", t)
    print("length =", length)
    print("n =", n)
    for i in range(n):
         print("i =", i)
         t.fd(length)
         t.lt(360 / n)

def circle(t, r):
    print("---- CIRCLE FRAME ----")
    print("t =", t)
    print("r =", r)
    circumference = 2 * math.pi * r
    print("circumference =", circumference)
    n = int(circumference / 3) + 3
    print("n =", n)
    length = circumference / n
    print("length =", length)
    polygon(t, length, n)

circle(bob, 100)
turtle.mainloop()
``````
# 2. The version of arc in Section 4.7 is not very accurate because the linear approximation of the circle is always outside the true circle. As a result, the Turtle ends up a few pixels away from the correct destination. My solution shows a way to reduce the effect of this error. Read the code and see if it makes sense to you. If you draw a diagram, you might see how it works.
`````Python
import turtle
import math
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def circle(t, r):
    arc(t, r, 360)

bob = turtle.Turtle()
circle(bob, 100)
turtle.mainloop()
``````

# Exercise 4.2. 

# Write an appropriately general set of functions that can draw flowers
`````Python
from __future__ import print_function, division
import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle
    n: number of line segments
    length: length of each segment
    angle: degrees to turn after each segment
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

def move(t, length):
    """Moves the turtle forward without leaving a trail.
    t: Turtle
    length: distance to move
    The pen is left down after the movement.
    """
    t.penup()
    t.forward(length)
    t.pendown()

# Create turtle
bob = turtle.Turtle()
# Draw three flowers
move(bob, -100)
flower(bob, 7, 60.0, 60.0)
move(bob, 100)
flower(bob, 10, 40.0, 80.0)
move(bob, 100)
flower(bob, 20, 140.0, 20.0)
# Hide turtle and keep window open
bob.hideturtle()
turtle.mainloop()
``````
# Exercise 4.3. 

# Write an appropriately general set of functions that can draw shapes
`````Python
from __future__ import print_function, division
import math
import turtle

def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)

def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    r: length of the equal legs
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

bob = turtle.Turtle()
bob.pu()
bob.bk(130)
bob.pd()

# draw polypies with various number of sides
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)

bob.hideturtle()
turtle.mainloop()
``````
# Exercise 4.4. 

# The letters of the alphabet can be constructed from a moderate number of basic elements,like vertical and horizontal lines and a few curves. Design an alphabet that can be drawn with a minimal number of basic elements and then write functions that draw the letters.

`````Python
from __future__ import print_function, division
import string
import turtle


"""
To use this typewriter, you have to provide a module named letters.py
that contains functions with names like draw_a, draw_b, etc.
"""

# check if the reader has provided letters.py
try:
    import letters
except ImportError as e:
    message = e.args[0]
    if message.startswith('No module'):
        raise ImportError(message + 
                          '\nYou have to provide a module named letters.py')


def teleport(t, x, y):
    """Moves the turtle without drawing a line.

    Postcondition: pen is down

    t: Turtle
    x: coordinate
    y: coordinate
    """
    t.pu()
    t.goto(x, y)
    t.pd()


def keypress(char):
    """Handles the event when a user presses a key.

    Checks if there is a function with the right name; otherwise
    it prints an error message.

    char: string, letter to draw
    """
    # if we're still drawing the previous letter, bail out
    if bob.busy:
        return
    else:
        bob.busy = True

    # figure out which function to call, and call it
    try:
        name = 'draw_' + char
        func = getattr(letters, name)
    except AttributeError:
        print("I don't know how to draw an", char)
        bob.busy = False
        return

    func(bob, size)

    letters.skip(bob, size/2)
    bob.busy = False


def carriage_return():
    """Moves to the beginning of the next line.
    """
    teleport(bob, -180, bob.ycor() - size*3)
    bob.busy = False


def presser(char):
    """Returns a function object that executes keypress.

    char: character to draw when the function is executed

    returns: function with no arguments
    """
    def func():
        keypress(char)
    return func


# create and position the turtle
size = 20
bob = turtle.Turtle()
bob.busy = False
teleport(bob, -180, 150)

# tell world to call keypress when the user presses a key
screen = bob.getscreen()

for char in string.ascii_lowercase:
    screen.onkey(presser(char), char)

screen.onkey(carriage_return, 'Return')
screen.listen()
turtle.mainloop()
``````
# Spiral
`````Python
from __future__ import print_function, division
import turtle

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.
    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)
    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta

# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=1000)
turtle.mainloop()
``````

# 5.1 Floor division and modulus

`````Python
a = 17
b = 5
print(a // b)  # floor division
print(a % b)   # modulus
``````

# A movie is 143 minutes long.
`````Python
a = 143
print(a//60)  # number of hours
print(a%60)   # number of minutes
``````
# Divisibility
`````Python
x = 20
print(x % 4)
print(x % 3)
``````
# Find the Last Digit
`````Python
x = 738
print(x % 10)
``````
# Last Two Digits
`````Python
x = 738
print(x % 100)
``````
# Split a number
`````Python
seconds = 367
minutes = seconds // 60
remaining_seconds = seconds % 60
print("Minutes:", minutes)
print("Remaining Seconds:", remaining_seconds)
``````
`````Python
number = 947
last_digit = number % 10
last_two_digits = number % 100
complete_groups_of_100 = number // 100
remaining_after_groups = number % 100
print("Last Digit:", last_digit)
print("Last Two Digits:", last_two_digits)
print("Complete Groups of 100:", complete_groups_of_100)
print("Remaining After Groups of 100:", remaining_after_groups)
``````
# 5.2 Boolean expressions (gives either True or False)
`````Python
print(10 == 10)
print(type(10) == type(10.0))

print(10 != 10)

x = 15
print(x > 10)

x = 15
print(x < 10)

x = 10
print(x >= 10)

x = 8
print(x <= 10)

x = 20
print(x == 20)
print(x != 20)
print(x > 15)
print(x < 15)

a = 25
b = 30
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 25)
print(b <= 30)
``````
# 5.3 Logical operators  and, or, not
`````Python
x = 5
print(x > 0 and x < 10)

x = 15
print(x < 10 or x == 15)

x = 8
print(not x > 10)

x = 12
print(x > 10 and x < 20)

x = 7
print(x < 5 or x > 10)

x = 20
print(not (x == 20))

x = 12
print(x > 5 and x < 10 or x == 12)

x = 18
print((x > 10 and x < 20) or x == 5)

x = 15
print(not (x < 10 or x > 20))
``````
# 5.4 Conditional execution
`````Python
x = 10
y = 20
if x > 0:
    print('x is positive')
``````
# 5.5 Alternative execution
`````Python
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
``````
# 5.6 Chained conditionals
`````Python
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
``````
# 5.7 Nested conditionals
`````Python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
``````
# 5.8 Recursion
`````Python
def countdown(n):
    n = int(n)  # Ensure n is an integer
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(25)
``````
